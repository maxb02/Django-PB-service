
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .sncheck import sn_shipments, sn_validator, region_ceker, region_mistmatch_notifier, serial_number_check_journal, \
    is_not_old_device
from .models import SerialNumberCheckJournal

@login_required
def serialcheck(request):
    if request.method == "POST":
        serial_number = request.POST['sn'].strip().upper()
        is_valid = sn_validator(serial_number)
        device_info = sn_shipments(serial_number)
        is_region_match = region_ceker(request.user, device_info)
        user = request.user
        if not user.is_staff:
            serial_number_check_journal(serial_number, user, is_valid, is_region_match)
        if not is_region_match and not (user.groups.filter(name='moderator').exists() or user.is_staff) and is_not_old_device(device_info):
            region_mistmatch_notifier(serial_number, device_info[0], request.user, request.LANGUAGE_CODE)

        return render(request, 'sncheck/sncheck.html', {'serial_number': serial_number,
                                                        'is_valid': is_valid,
                                                        'device_info': device_info,
                                                        })
    else:
        return render(request, 'sncheck/sncheck.html')


@login_required
def snchecklist(request):
    if request.method == 'POST':
        serial_numbers = request.POST['serial_numbers'].replace(' ', '')
        serial_numbers_list = serial_numbers.strip().upper().splitlines()
        devices_info_list = []
        for serial_number in serial_numbers_list:
            is_valid = sn_validator(serial_number)
            device_info = sn_shipments(serial_number)
            serial_number_journal = SerialNumberCheckJournal.objects.filter(serial_number=serial_number).distinct('user')
            devices_info_list.append({
                'serial_number': serial_number,
                'is_valid': is_valid,
                'device_info': device_info,
                'serial_number_journal' : serial_number_journal,
            })

        return render(request, 'sncheck/snchecklist.html', {'devices_info_list': devices_info_list,
                                                            'serial_numbers': serial_numbers})

    return render(request, 'sncheck/snchecklist.html')


