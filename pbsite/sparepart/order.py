from sparepart.cart import Cart
from sparepart.forms import OrderCreateForm
from sparepart.models import OrderSupplier, Supplier, OrderItem


class CartIsEmptyException(Exception):
    pass


def create_order(request):
    cart = Cart(request)
    if cart:
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.created_by = request.user
            order.save()
            for supplier_name, spare_parts_list in cart.get_items_by_supplier().items():
                order_supplier = OrderSupplier.objects.create(
                    order=order,
                    supplier=Supplier.objects.get(name=supplier_name), )
                for item in spare_parts_list:
                    OrderItem.objects.create(order_supplier=order_supplier,
                                             spare_part=item['spare_part'],
                                             price=item['price'],
                                             quantity=item['quantity'])
            cart.clear()
            return order
    raise CartIsEmptyException
