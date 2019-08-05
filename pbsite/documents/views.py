from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.rendering import render_to_pdf_response
from .forms import ActRequestForm, ActComentForm
from .models import Act
from django.http import HttpResponse


class DocumentRequest(LoginRequiredMixin, View):
    def post(self, request):
        form = ActRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_act = form.save(commit=False)
            new_act.created_by = request.user
            form.save()
            new_act.add_number()
            return redirect('document_list_url')

        else:
            return render(request, 'documents/document_request_form.html', {'form': form})

    def get(self, request):
        form = ActRequestForm
        return render(request, 'documents/document_request_form.html', {'form': form})


@login_required
def document_list(request):
    documents = Act.objects.all()
    if not request.user.is_staff:
        documents = documents.filter(created_by__service_center=request.user.service_center)
    return render(request, 'documents/document_list.html', {'documents': documents})


class DocumentDetail(LoginRequiredMixin, View):
    def post(self, request, number):
        document = get_object_or_404(Act, number=number)
        form = ActComentForm(request.POST, instance=document)
        if 'accept' in request.POST:
            document.status = 'confirmed'
        elif 'reject' in request.POST:
            document.status = 'rejected'
        document.accepted_or_declined_by = request.user
        document.conclusion_date = datetime.now()
        if form.is_valid():
            document.save()
        return redirect('document_list_url')

    def get(self, request, number):
        document = get_object_or_404(Act, number=number)
        if request.user.is_staff:
            form = ActComentForm(instance=document)
            return render(request, 'documents/document_detail.html', {'document': document, 'form': form})
        elif document.created_by.service_center != request.user.service_center:
            raise PermissionDenied
        return render(request, 'documents/document_detail.html', {'document': document, })


@login_required
def generate_pdf(request, number):
    document = get_object_or_404(Act, number=number)
    if document.status == 'confirmed' and (
            document.created_by.service_center == request.user.service_center or request.user.is_staff):
        language = document.created_by.service_center.language
        template = document.document_type
        context = {'document': document, }
        return render_to_pdf_response(request, 'documents/pdf/{}_{}.html'.format(language, template), context, )
    else:
        raise PermissionDenied
