from django.contrib.auth import get_user_model
from django.test import TestCase

from sparepart.cart import Cart
from sparepart.models import SparePart, Supplier, Manufacturer, Order, OrderSupplier, OrderItem
from sparepart.order import create_order, CartIsEmptyException


class CreateOrderTest(TestCase):
    def setUp(self):
        self.request = self.client.request()
        self.request.session = self.client.session
        self.destination = 'Destination'

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username='testuser', password='12345')
        cls.supplier1_id = Supplier.objects.create(name='Supplier1').id
        cls.supplier2_id = Supplier.objects.create(name='Supplier2').id
        manufacturer = Manufacturer.objects.create(name='Manufacturer')
        supplier1 = Supplier.objects.get(id=cls.supplier1_id)
        supplier2 = Supplier.objects.get(id=cls.supplier2_id)

        cls.spare_part1_id = SparePart.objects.create(
            name='SparePart1',
            weight=100,
            size='22x33',
            sku='Spare_Part_SKU1',
            description='Some Description1',
            supplier=supplier1,
            manufacturer=manufacturer,
            purchase_price=9.99
        ).id

        cls.spare_part2_id = SparePart.objects.create(
            name='SparePart2',
            weight=100,
            size='22x33',
            sku='Spare_Part_SKU2',
            description='Some Description2',
            supplier=supplier2,
            manufacturer=manufacturer,
            purchase_price=19.99
        ).id

    def test_cart_is_empty_exception(self):
        cart = Cart(self.request)
        user = get_user_model().objects.first()
        with self.assertRaises(CartIsEmptyException):
            create_order(cart, user, self.destination)

    def test_order_creation(self):
        user = get_user_model().objects.first()
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        self.assertFalse(Order.objects.exists(), 'There are no order yet')
        order = create_order(cart, user, self.destination)
        self.assertTrue(Order.objects.exists(), "Order was created")
        self.assertEquals(Order.objects.first(), order)
        self.assertEquals(Order.objects.first().created_by, user, 'Order "created_by" field has a wrong value')
        self.assertEquals(order.orders_supplier.count(), 2, 'Order should by connected with two OrderSupplier item')
        self.assertEquals(OrderSupplier.objects.count(), 2, 'Order should create two OrderSupplier item')
        self.assertTrue(Order.objects.filter(orders_supplier__order_items__spare_part__id=spare_part1.id).exists(),
                        'First SparePart should be in order')
        self.assertTrue(Order.objects.filter(orders_supplier__order_items__spare_part__id=spare_part2.id).exists(),
                        'Second SparePart should be in order')
        self.assertTrue(Order.objects.filter(orders_supplier__supplier=Supplier.objects.get(id=self.supplier1_id)),
                        'First Supplier should be in Order')
        self.assertTrue(Order.objects.filter(orders_supplier__supplier=Supplier.objects.get(id=self.supplier2_id)),
                        'Second Supplier should be in Order')
        self.assertEquals(OrderItem.objects.get(spare_part=spare_part1).price,
                          spare_part1.purchase_price)

