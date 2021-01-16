from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView

from device.exceptions import SKUDoesNotExist
from device.mixins import DeviceModelFieldMixin
from users.mixins import UserServiceCenterObjectOnlyMixin
from .label import get_info_for_label, create_label_response
from .models import RefurbishmentDevice
from .forms import RefurbishmentDeviceForm


class RefurbishmentDeviceList(PermissionRequiredMixin,
                              LoginRequiredMixin,
                              UserServiceCenterObjectOnlyMixin,
                              DeviceModelFieldMixin,
                              ListView):
    model = RefurbishmentDevice
    permission_required = 'refurbishment.view_refurbishment_device_list'
    raise_exception = True
    queryset = RefurbishmentDevice.objects.prefetch_related('refurbishment').select_related(
        'created_by__service_center', 'condition', )
    serial_number_field = 'new_serial_number'
    user_field = 'created_by'


class RefurbishmentDeviceCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = RefurbishmentDevice
    form_class = RefurbishmentDeviceForm
    template_name = 'refurbishment/refurbishmentdevice_create_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(RefurbishmentDeviceCreate, self).form_valid(form)


class RefurbishmentDeviceDetail(LoginRequiredMixin, UserServiceCenterObjectOnlyMixin, DetailView):
    model = RefurbishmentDevice
    user_field = 'created_by'


class RefurbishmentDeviceUpdate(LoginRequiredMixin, UserServiceCenterObjectOnlyMixin, UpdateView):
    model = RefurbishmentDevice
    template_name = 'refurbishment/refurbishmentdevice_update_form.html'
    form_class = RefurbishmentDeviceForm
    raise_exception = True
    user_field = 'created_by'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        if 'was_returned' in self.request.POST:
            if not self.request.user.has_perm('can_mark_refurbishment_device_as_returned'):
                raise PermissionDenied()
            form.instance.was_returned = True
        return super(RefurbishmentDeviceUpdate, self).form_valid(form)


def get_label(request, pk, ):
    if request.method == 'GET':
        try:
            info = get_info_for_label(pk)
        except SKUDoesNotExist as e:
            raise Http404('{}, please contact admin'.format(e))
        number = int(request.GET.get('n', 1))
        label = create_label_response(info, number=number)
        return label
