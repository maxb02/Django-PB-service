import requests
import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import EmailForNotifications, AllowedDeviceRegion, SerialNumberCheckJournal


def validate_serial_number(serial_number):
    '''Check the serial number for valid'''

    if serial_number:
        try:
            r = requests.get(settings.SERIAL_NUMBER_VALIDATOR_URL, params={'sn': serial_number}, verify=False)
        except:
            return 'Error'
        if r.status_code != 200:
            return 'Error'
        elif 'No such key' in r.text:
            return False
        else:
            return True


def get_device_info_from_shipments(serial_number):
    '''Request device info from shipments.
    Converting into datetime shippingDate & productionDate.
    Because shipments database can store several records for one serial number this returns the list of dictionaries.
    '''
    if serial_number:
        try:
            device_info = requests.get(settings.SERIAL_NUMBER_SHIPMENTS_URL, params={'sn': serial_number},
                                       verify=False).json()
        except:
            return 'Error'
        if device_info:
            for record in device_info:
                record['shippingDate'] = datetime.datetime.strptime(record['shippingDate'], "%Y-%m-%d %H:%M:%S")
                record['productionDate'] = datetime.datetime.strptime(record['month'] + record['year'], '%m%Y')
                record['serialNumber'] = serial_number
            return device_info
        else:
            return False


def check_device_and_user_allowed_regions(user, device_info):
    '''Compare user allowed region with the device region'''
    if device_info:
        for record in device_info:
            if AllowedDeviceRegion.objects.filter(user_region__in=user.groups.all(),
                                                  device_region=record['countryEng']).exists():
                return True
            else:
                return False


def send_region_mismatch_letter(device_data, user, language):
    '''Send the region mismatch letter to user and service center manager if it exists'''
    subject = 'Region Mismatch {}'.format(device_data['serialNumber'], )
    from_email = settings.EMAIL_FROM
    to = [user.email]
    cc = list(EmailForNotifications.objects.filter(user_region__in=user.groups.all()).all())
    if language == 'ru' or language == 'ua':
        email_template = 'sncheck/letters/region_mismatch_notifier_letter_ru.html'
    else:
        email_template = 'sncheck/letters/region_mismatch_notifier_letter_en.html'

    html_content = get_template(email_template).render(
        {
            'device_data': device_data,
            'user': user,
        })
    msg = EmailMessage(subject, html_content, from_email, to, cc=cc, )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def add_record_to_serial_number_check_journal(serial_number, user, is_valid, is_region_match):
    '''Add the record to journal'''
    if is_valid == "Error":
        is_valid = None
    if is_region_match == 'Error':
        is_region_match = None
    SerialNumberCheckJournal.objects.create(serial_number=serial_number, user=user, is_valid=is_valid,
                                            is_region_match=is_region_match)


def is_not_old_device(device_info):
    '''Return true if the device is not older than 900 days from product and shipping dates'''
    if device_info:
        for record in device_info:
            if (datetime.datetime.today() - record['shippingDate']).days > 900 or (
                    datetime.datetime.today() - record['productionDate']).days > 900:
                return False
        return True
