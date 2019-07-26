from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .sncheck import get_device_info_from_shipments, validate_serial_number, check_device_and_user_allowed_regions, \
    send_region_mismatch_letter, add_record_to_serial_number_check_journal, \
    is_not_old_device
from .models import SerialNumberCheckJournal
from documents.models import Act


class SerialNumberCheck(LoginRequiredMixin, View):
    """Viev for serial number check from item form"""

    def post(self, request):
        serial_number = request.POST.get('sn', '').strip().upper()
        is_valid = validate_serial_number(serial_number)
        device_info = get_device_info_from_shipments(serial_number)
        user = request.user
        is_region_match = check_device_and_user_allowed_regions(user, device_info)
        user = request.user
        if not user.is_staff:
            add_record_to_serial_number_check_journal(serial_number, user, is_valid, is_region_match)
        if not is_region_match and not (
                user.groups.filter(name='moderator').exists() or user.is_staff) and is_not_old_device(device_info):
            send_region_mismatch_letter(device_info[0], request.user, request.LANGUAGE_CODE)

        return render(request, 'sncheck/serial_number_check.html', {'serial_number': serial_number,
                                                                    'is_valid': is_valid,
                                                                    'device_info': device_info,
                                                                    })

    def get(self, request):
        return render(request, 'sncheck/serial_number_check.html')


class SerialNumberInfo(LoginRequiredMixin, View):
    '''Viev for order info about serial number from link'''

    def get(self, request, serial_number):
        if serial_number:
            is_valid = validate_serial_number(serial_number)
            device_info = get_device_info_from_shipments(serial_number)
            documents = Act.objects.filter(serial_number=serial_number).all()
            return render(request, 'sncheck/serial_number_info.html', {'serial_number': serial_number,
                                                                       'is_valid': is_valid,
                                                                       'device_info': device_info,
                                                                       'documents': documents
                                                                       })
        else:
            raise Http404


@login_required
def snchecklist(request):
    if request.method == 'POST':
        serial_numbers = request.POST['serial_numbers'].replace(' ', '')
        serial_numbers_list = serial_numbers.strip().upper().splitlines()
        devices_info_list = []
        for serial_number in serial_numbers_list:
            is_valid = validate_serial_number(serial_number)
            device_info = get_device_info_from_shipments(serial_number)
            serial_number_journal = SerialNumberCheckJournal.objects.filter(serial_number=serial_number).distinct(
                'user')
            devices_info_list.append({
                'serial_number': serial_number,
                'is_valid': is_valid,
                'device_info': device_info,
                'serial_number_journal': serial_number_journal,
            })

        return render(request, 'sncheck/serial_number_check_list.html', {'devices_info_list': devices_info_list,
                                                                         'serial_numbers': serial_numbers})

    return render(request, 'sncheck/serial_number_check_list.html')
