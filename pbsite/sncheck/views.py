from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .snshipments import sn_shipments
from .snvalidator import snvalidator
from .region_checker import region_ceker
from .region_mismatch_notifier import region_mistmatch_notifier


@login_required
def serialcheck(request):
    if request.method == "POST":
        serial_number = request.POST['sn'].strip().upper()
        is_valid = snvalidator(serial_number)
        device_info = sn_shipments(serial_number)
        if not region_ceker(request.user, device_info):
            region_mistmatch_notifier(serial_number, device_info[0], request.user, request.LANGUAGE_CODE)

        return render(request, 'sncheck/sncheck.html', {'serial_number': serial_number,
                                                 'is_valid': is_valid,
                                                        'device_info': device_info,
                                                        })
    else:
        return render(request, 'sncheck/sncheck.html')
