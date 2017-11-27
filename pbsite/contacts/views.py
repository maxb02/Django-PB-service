from django.shortcuts import render
from .models import Country
from .models import Email
from .models import Link
from django.contrib.auth.decorators import login_required


@login_required
def contacts(request):
    countrys = Country.objects.order_by('name')
    emails = Email.objects.all()
    links = Link.objects.all()
    return render(request, 'contacts/contacts.html', {'countrys' : countrys,
                                                      'emails' : emails,
                                                      'links' : links
    })