from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import ActRequestForm
from .models import Act, SerialNumberPrefix
from django.http import HttpResponse
from sncheck.sncheck import sn_shipments


@login_required
def requestform(request):
    if request.method == 'POST':
        form = ActRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_act = form.save(commit=False)
            new_act.created_by = request.user
            form.save()

            return redirect('showall')

        else:
            return HttpResponse('Form not valid')

    else:
        form = ActRequestForm
        return render(request, 'documents/request_form.html', {'form': form})


@login_required
def showall(request):
    if request.user.is_staff:
        acts = Act.objects.all()
        return render(request, 'documents/showall.html', {'acts' : acts})
    else:
        acts = Act.objects.filter(created_by=request.user)
        return render(request, 'documents/showall.html', {'acts': acts})

@login_required
def act(request, id):
    act = Act.objects.get(id=id)
    if request.method == 'POST':
        if 'accept' in request.POST:
            act.status = 'confirmed'
            act.save()
            return redirect('showall')
        elif 'reject' in request.POST:
            act.status = 'rejected'
            act.save()
            return redirect('showall')
    if request.user.is_staff:
        return render(request, 'documents/act.html', {'act': act})

    elif act.created_by == request.user:
        return render(request, 'documents/act.html', {'act': act})

def getpdf(request, id):
    act = Act.objects.get(id=id)
    if act.status == 'confirmed':
        return render(request, 'documents/pdftemplates/outofwaranty.html')


