from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from easy_pdf.rendering import render_to_pdf_response
from .forms import ActRequestForm, ActComentForm
from .models import Act
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
    acts = Act.objects.all().order_by('-filling_date')
    if request.user.is_staff:
        return render(request, 'documents/showall.html', {'acts' : acts})
    else:
        acts = acts.filter(created_by__service_center = request.user.service_center)
        return render(request, 'documents/showall.html', {'acts': acts})

@login_required
def act(request, id):
    act = Act.objects.get(id=id)
    form = ActComentForm(request.POST,instance=act)
    if request.method == 'POST':
        if 'accept' in request.POST:
            act.status = 'confirmed'
        elif 'reject' in request.POST:
            act.status = 'rejected'
        act.accepted_or_declined_by = request.user
        act.conclusion_date = datetime.now()
        act.accepted_or_declined_by = request.user
        if form.is_valid():
            act.save()
        return redirect('showall')

    if request.user.is_staff:
        form = ActComentForm(instance=act)
        return render(request, 'documents/act.html', {'act': act, 'form': form})

    elif act.created_by == request.user:
        return render(request, 'documents/act.html', {'act': act})

@login_required
def getpdf(request, id):
    act = Act.objects.get(id=id)
    if act.status == 'confirmed' and (act.created_by.service_center == request.user.service_center or request.user.is_staff):
        language = act.created_by.service_center.language
        template = act.document_type
        context = {'act': act,}
        return render_to_pdf_response(request, 'documents/pdf/{}_{}.html'.format(language, template), context,)

