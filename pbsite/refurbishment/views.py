from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import RefurbishmentDevice
from .forms import RefurbishmentDeviceForm


class RefurbishmentDeviceList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = RefurbishmentDevice
    permission_required = 'refurbishment.view_refurbishment_device_list'
    raise_exception = True
    def get_queryset(self):
        queryset = super(RefurbishmentDeviceList, self).get_queryset().prefetch_related('refurbishment').select_related(
            'created_by__service_center', 'condition')
        if not self.request.user.is_staff:
            queryset = queryset.filter(created_by__service_center=self.request.user.service_center).select_related(
                'created_by__service_center', 'updated_by')
        return queryset


class RefurbishmentDeviceCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = RefurbishmentDevice
    form_class = RefurbishmentDeviceForm
    template_name = 'refurbishment/refurbishmentdevice_create_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(RefurbishmentDeviceCreate, self).form_valid(form)




class RefurbishmentDeviceDetail(LoginRequiredMixin, DetailView):
    model = RefurbishmentDevice

    def get_queryset(self):
        queryset = super(RefurbishmentDeviceDetail, self).get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(created_by__service_center=self.request.user.service_center).select_related(
                'created_by__service_center', 'updated_by__service_center')
        return queryset


class RefurbishmentDeviceUpdate(LoginRequiredMixin, UpdateView):
    model = RefurbishmentDevice
    template_name = 'refurbishment/refurbishmentdevice_update_form.html'
    form_class = RefurbishmentDeviceForm
    raise_exception = True
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        if 'was_returned' in self.request.POST:
            if not self.request.user.has_perm('can_mark_refurbishment_device_as_returned'):
                raise PermissionDenied()
            form.instance.was_returned = True
        return super(RefurbishmentDeviceUpdate, self).form_valid(form)

    def get_queryset(self):
        queryset = super(RefurbishmentDeviceUpdate, self).get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(created_by__service_center=self.request.user.service_center).select_related(
                'created_by__service_center', 'updated_by')
        return queryset
