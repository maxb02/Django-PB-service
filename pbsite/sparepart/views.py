from collections import defaultdict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, View

from device.models import Device
from .cart import Cart
from .forms import CartAddSparePartForm
from .models import SparePart


class SparePartDetail(LoginRequiredMixin, DetailView):
    model = SparePart


class SparePartDeviceList(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(Device.objects.prefetch_related('spare_parts__category'), pk=pk)
        categories = defaultdict(list)

        for spare_part in device.spare_parts.all():
            categories[spare_part.category.name].append(spare_part)

        cart_spare_part_form = CartAddSparePartForm()

        return render(request, 'sparepart/sparepart_list.html', {
            'device': device,
            'categories': dict(categories),
            'cart_spare_part_form': cart_spare_part_form
        })


# Cart__________________________________________________________
@require_POST
def cart_add(request, spare_part_id):
    cart = Cart(request)
    spare_part = get_object_or_404(SparePart, id=spare_part_id)
    form = CartAddSparePartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            spare_part=spare_part,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, spare_part_id):
    cart = Cart(request)
    spare_part = get_object_or_404(SparePart, id=spare_part_id)
    cart.remove(spare_part)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddSparePartForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    return render(request, 'sparepart/cart_detail.html', {'cart': cart})
# ________________________________________________________________________
