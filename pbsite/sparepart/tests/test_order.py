from django.contrib.auth import get_user_model
from django.test import TestCase

from sparepart.cart import Cart
from sparepart.models import SparePart, Supplier, Manufacturer, Order, OrderSupplier
from sparepart.order import create_order, CartIsEmptyException


class CreateOrderTest(TestCase):
    def setUp(self):
        self.request = self.client.request()
        self.request.session = self.client.session
        self.destination = 'Destination'

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username='testuser', password='12345')
        supplier1 = Supplier.objects.create(name='Supplier1')
        supplier2 = Supplier.objects.create(name='Supplier2')
        manufacturer = Manufacturer.objects.create(name='Manufacturer')

        SparePart.objects.create(
            name='SparePart1',
            weight=100,
            size='22x33',
            sku='Spare_Part_SKU1',
            description='Some Description1',
            supplier=supplier1,
            manufacturer=manufacturer,
            purchase_price=9.99
        )

        SparePart.objects.create(
            name='SparePart2',
            weight=100,
            size='22x33',
            sku='Spare_Part_SKU2',
            description='Some Description2',
            supplier=supplier2,
            manufacturer=manufacturer,
            purchase_price=19.99
        )

    def test_cart_is_empty_exception(self):
        cart = Cart(self.request)
        user = get_user_model().objects.first()
        with self.assertRaises(CartIsEmptyException):
            create_order(cart, user, self.destination)

    def test_order_creation(self):
        user = get_user_model().objects.first()
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=1)
        spare_part2 = SparePart.objects.get(id=2)
        cart.add(spare_part1)
        cart.add(spare_part2)
        order = create_order(cart, user, self.destination)
        self.assertTrue(Order.objects.exists(), "Order wasn't created")
        self.assertEquals(Order.objects.first(), order)
        self.assertEquals(Order.objects.first().created_by, user, 'Order "created_by" field has a wrong value')
        self.assertEquals(OrderSupplier.objects.count(), 2, 'Order should create two OrderSupplier item')
        self.assertIn(OrderSupplier.objects.get(id=1), order.orders_supplier.all(),
                      'First OrderSupplier should be in Order')
        self.assertIn(OrderSupplier.objects.get(id=2), order.orders_supplier.all(),
                      'Second OrderSupplier should be in Order')
        self.assertEquals(OrderSupplier.objects.get(id=1).order_items.get(id=1).spare_part, spare_part1,
                          'First SparePart should be in first OrderSupplier item')
        self.assertEquals(OrderSupplier.objects.get(id=2).order_items.get(id=2).spare_part, spare_part2,
                          'Second SparePart should be in second OrderSupplier item')

        self.assertEquals(OrderSupplier.objects.get(id=1).order_items.get(id=1).order_supplier.supplier.name,
                          spare_part1.supplier.name,
                          'First Supplier should be in first OrderSupplier')
        self.assertEquals(OrderSupplier.objects.get(id=2).order_items.get(id=2).order_supplier.supplier.name,
                          spare_part2.supplier.name,
                          'Second Supplier should be in second OrderSupplier')

        self.assertEquals(OrderSupplier.objects.get(id=1).order_items.get(id=1).price,
                          spare_part1.purchase_price)
        self.assertEquals(OrderSupplier.objects.get(id=2).order_items.get(id=2).price,
                          spare_part2.purchase_price)
