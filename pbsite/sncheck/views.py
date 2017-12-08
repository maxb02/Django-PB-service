from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .snshipments import *
from .snvalidator import *

@login_required
def serialcheck(request):
    return render(request, 'sncheck/sncheck.html')

@login_required
def sndetail(request):
    serial_number = request.GET['sn']
    is_valid = snvalidator(serial_number)
    info = sn_shipments(serial_number)
    return render(request, 'sncheck/sndetail.html', {'serial_number': serial_number,
                                             'is_valid': is_valid,
                                             'info': info,
                                                     })