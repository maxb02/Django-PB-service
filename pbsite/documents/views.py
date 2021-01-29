from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.rendering import render_to_pdf_response
from .forms import ActRequestForm, ActCommentForm, ActCompensationStatusForm
from .models import Act
from users.mixins import UserServiceCenterObjectOnlyMixin, CreatedByUserMixin
from device.mixins import DevicesListAddModelNumberFieldMixin, DeviceAddModelNumberFieldMixin


class ActCreate(LoginRequiredMixin, CreatedByUserMixin, CreateView):
    raise_exception = True
    model = Act
    form_class = ActRequestForm
    template_name = 'documents/document_request_form.html'


class ActDetail(LoginRequiredMixin,
                DeviceAddModelNumberFieldMixin,
                UserServiceCenterObjectOnlyMixin,
                DetailView):
    model = Act
    user_field = 'created_by'
    raise_exception = True
    slug_field = 'number'
    slug_url_kwarg = 'number'
    queryset = Act.objects.select_related('created_by__service_center')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm('documents.accept_or_decline_acts'):
            context['form'] = ActCommentForm
            context['compensation_status_form'] = ActCompensationStatusForm(instance=self.object)
        return context


class ActList(LoginRequiredMixin,
              DevicesListAddModelNumberFieldMixin,
              UserServiceCenterObjectOnlyMixin,
              ListView):
    model = Act
    raise_exception = True
    queryset = Act.objects.select_related('created_by__service_center')
    user_field = 'created_by'


class ActAcceptOrReject(LoginRequiredMixin, View):
    def post(self, request, number):
        document = get_object_or_404(Act, number=number)
        form = ActCommentForm(request.POST, instance=document)
        if 'accept' in request.POST:
            document.status = 'confirmed'
        elif 'reject' in request.POST:
            document.status = 'rejected'
        document.accepted_or_declined_by = request.user
        document.conclusion_date = datetime.now()
        if form.is_valid():
            document.save()
        return redirect('document_list_url')


class ActCompensationStatusUpdate(LoginRequiredMixin,
                                  UserServiceCenterObjectOnlyMixin,
                                  UpdateView):
    model = Act
    form_class = ActCompensationStatusForm



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
