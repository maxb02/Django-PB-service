from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .snshipments import *
from .snvalidator import *
from .regionmismatch import *

from .models import EmailForNotifications

@login_required
def serialcheck(request):
    return render(request, 'sncheck/sncheck.html')

@login_required
def sndetail(request):
    serial_number = request.GET['sn'].strip().upper()
    is_valid = snvalidator(serial_number)
    # info = sn_shipments(serial_number)
    info = [{"shippingDate": "2015-03-21 12:00:00", "manufacturer": "Yitoa", "partner": "PB Readers",
      "partnerCountry": "Germany", "device": "PocketBook Touch Lux 2", "model": "PB626", "year": "2015", "month": "01",
      "country": "\u0412\u0435\u0441\u044c \u043c\u0438\u0440", "color": "\u0411\u0435\u043b\u044b\u0439",
      "countryEng": "WorldWide", "colorEng": "White"}]

    if not (request.user.groups.filter(name= 'moderator').exists() or request.user.is_superuser):
        for data in info:
            if not request.user.groups.filter(name= data['countryEng']).exists():
                regionmismatch(serial_number, data['countryEng'], request.user, list(EmailForNotifications.objects.all()))

    return render(request, 'sncheck/sndetail.html', {'serial_number': serial_number,
                                             'is_valid': is_valid,
                                             'info': info,
                                                     })