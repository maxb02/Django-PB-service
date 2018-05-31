import requests
import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import EmailForNotifications, AllowedDeviceRegion, SerialNumberCheckJournal


def sn_validator(sn):
    if sn:
        try:
            key = requests.get(settings.SERIAL_NUMBER_VALIDATOR_URL, params={'sn': sn}, verify=False).text
        except:
            return 'Erorr'
        if key == ' No such key':
            return False
        else:
            return True


def sn_shipments(sn):
    if sn:
        try:
            device_info = requests.get(settings.SERIAL_NUMBER_SHIPMENTS_URL, params={'sn': sn}, verify=False).json()
            # device_info = [{"shippingDate":"2015-03-21 12:00:00","manufacturer":"Yitoa","partner":"PB Readers","partnerCountry":"Germany","device":"PocketBook Touch Lux 2","model":"PB626","year":"2015","month":"01","country":"\u0412\u0435\u0441\u044c \u043c\u0438\u0440","color":"\u0411\u0435\u043b\u044b\u0439","countryEng":"CIS","colorEng":"White"}]
        except:
            return 'Erorr'
        if device_info:
            for element in device_info:
                element['shippingDate'] = datetime.datetime.strptime(element['shippingDate'], "%Y-%m-%d %H:%M:%S")
            return device_info
        else:
            return False


def region_ceker(user, device_info):
    if not device_info or device_info == 'Erorr':
        return 'Erorr'

    for device_data in device_info:
        if AllowedDeviceRegion.objects.filter(
                user_region=user.groups.all(), device_region=device_data['countryEng']).exists():
            return True
        else:
            return False


def region_mistmatch_notifier(serial_number, device_data, user, language):
    subject = 'Region Mismatch {}'.format(serial_number, )
    from_email = 'noreplay@service.pocketbook-int.com'
    to = [user.email]
    cc = list(EmailForNotifications.objects.filter(user_region=user.groups.all()).all())
    if language == 'ru' or language == 'ua':
        emai_template = 'sncheck/region_mismatch_notifier_letter_ru.html'
    else:
        emai_template = 'sncheck/region_mismatch_notifier_letter_en.html'

    html_content = get_template(emai_template).render(
        {'serial_number': serial_number,
         'device_data': device_data,
         'user' : user,
         })
    msg = EmailMessage(subject, html_content, from_email, to, cc=cc,)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def serial_number_check_journal(serial_number, user, is_valid, is_region_match):
    if is_valid == "Erorr":
        is_valid = None
    if is_region_match == 'Erorr':
        is_region_match = None
    SerialNumberCheckJournal.objects.create(serial_number= serial_number, user= user, is_valid = is_valid, is_region_match= is_region_match)
