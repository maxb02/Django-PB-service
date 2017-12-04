from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .snshipments import *
from .snvalidator import *

@login_required
def serialcheck(request):
    return render(request, 'sncheck/sncheck.html')

def sndetail(request):
    seial_number = request.GET['sn']
    is_valid = snvalidator(seial_number)
    info = sn_shipments(seial_number)
    return render(request, 'sncheck/sndetail.html', {'seial_number': seial_number,
                                             'is_valid': is_valid,
                                             'info': info,
                                                     })