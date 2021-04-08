from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.rendering import render_to_pdf_response

from device.models import Device
from device.serial_number_parser import parse_serial_number
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


class ActGeneratePDF(LoginRequiredMixin,
                     View):

    def get(self, request, number):
        obj = get_object_or_404(Act, number=number)
        if not obj.status == 'confirmed':
            raise PermissionDenied
        serial_number = obj.serial_number
        parsed_serial_number = parse_serial_number(serial_number)
        try:
            device = Device.objects.values('model_number').get(code=parsed_serial_number.model_code,
                                                               factory__code=parsed_serial_number.factory_code)
            model_number = device.get('model_number')
        except Device.DoesNotExist:
            model_number = None
        obj.model_number = model_number
        language = obj.created_by.service_center.language
        template = obj.document_type
        context = {'document': obj, }
        return render_to_pdf_response(request, 'documents/pdf/{}_{}.html'.format(language, template), context, )
