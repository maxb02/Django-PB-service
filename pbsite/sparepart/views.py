from collections import defaultdict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, View, ListView

from device.models import Device
from users.mixins import UserServiceCenterObjectOnlyMixin
from .cart import Cart
from .forms import CartAddSparePartForm, OrderCreateForm
from .models import SparePart, Order, OrderSupplier
from .order import create_order, get_supplier_order_file_response


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


class OrderCreateView(LoginRequiredMixin,
                      View):
    def post(self, request):
        order = create_order(request)
        return HttpResponseRedirect(reverse('order_created', kwargs={'pk': order.pk}))

    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm()
        return render(request,
                      'sparepart/order_create.html', {'form': form,
                                                      'cart': cart})


class OrderCreatedView(LoginRequiredMixin,
                       UserServiceCenterObjectOnlyMixin,
                       DetailView):
    user_field = 'order__created_by'
    model = Order
    template_name = 'sparepart/order_created.html'


class OrderSupplierDetailView(LoginRequiredMixin,
                              UserServiceCenterObjectOnlyMixin,
                              DetailView):
    user_field = 'order__created_by'
    model = OrderSupplier
    template_name = 'sparepart/order_detail.html'


class OrderSupplierListView(LoginRequiredMixin,
                            UserServiceCenterObjectOnlyMixin,
                            ListView):
    user_field = 'order__created_by'
    model = OrderSupplier
    template_name = 'sparepart/order_list.html'


def order_supplier_file(request, pk):
    order = get_object_or_404(OrderSupplier, pk=pk)
    response = get_supplier_order_file_response(order)
    return response

