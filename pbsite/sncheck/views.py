from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .snshipments import *
from .snvalidator import *
from .regionmismatch import *

from .models import EmailForNotifications

@login_required
def serialcheck(request):
    if request.method == "POST":
        serial_number = request.POST['sn'].strip().upper()
        is_valid = snvalidator(serial_number)
        info = sn_shipments(serial_number)
        if not (request.user.groups.filter(name= 'moderator').exists() or request.user.is_superuser):
            for data in info:
                if not request.user.groups.filter(name= data['countryEng']).exists():
                    regionmismatch(serial_number, data['countryEng'], request.user, list(EmailForNotifications.objects.all()))

        return render(request, 'sncheck/sncheck.html', {'serial_number': serial_number,
                                                 'is_valid': is_valid,
                                                 'info': info,
                                                         })
    else:
        return render(request, 'sncheck/sncheck.html')
