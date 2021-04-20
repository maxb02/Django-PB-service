from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
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


def get_supplier_order_file_response(supplier_order):
    file_name = '{}_{}_order_{}.xls'.format(supplier_order.supplier.name, supplier_order.id, supplier_order.update_date)
    wb = Workbook()
    ws1 = wb.active
    ws1.title = 'order'
    ws1.append(('Part Number', 'Name', 'Quantity'))

    for item in supplier_order.order_items.all():
        ws1.append((str(item.spare_part.sku), str(item.spare_part.name), str(item.quantity)))

    response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    return response

