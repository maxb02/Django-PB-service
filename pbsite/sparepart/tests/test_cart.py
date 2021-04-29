from decimal import Decimal

from django.test import TestCase
from sparepart.cart import Cart
from sparepart.models import SparePart, Supplier, Manufacturer
from django.conf import settings


class CartTest(TestCase):

    def setUp(self):
        self.request = self.client.request()
        self.request.session = self.client.session

    @classmethod
    def setUpTestData(cls):
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

    def test_cart_is_empty_when_created(self):
        cart = Cart(self.request)
        self.assertEquals(len(cart.cart), 0)

    def test_add_to_cart(self):
        cart = Cart(self.request)
        spare_part = SparePart.objects.get(id=self.spare_part1_id)
        cart.add(spare_part)
        self.assertEquals(len(cart.cart), 1)
        self.assertIn(str(spare_part.id), cart.cart)
        self.assertEquals(cart.cart['1']['price'], str(spare_part.purchase_price))
        self.assertEquals(cart.cart['1']['quantity'], 1)

    def test_add_item_twice(self):
        cart = Cart(self.request)
        spare_part = SparePart.objects.get(id=self.spare_part1_id)
        cart.add(spare_part)
        cart.add(spare_part, quantity=5)
        self.assertEquals(len(cart.cart), 1)
        self.assertEquals(cart.cart['1']['quantity'], 6)

    def test_add_update_quantity(self):
        cart = Cart(self.request)
        spare_part = SparePart.objects.get(id=self.spare_part1_id)
        cart.add(spare_part)
        self.assertEquals(cart.cart['1']['quantity'], 1)
        cart.add(spare_part, quantity=3, update_quantity=True)
        self.assertEquals(cart.cart['1']['quantity'], 3)

    def test_add_two_items(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        self.assertEquals(len(cart.cart), 2)
        self.assertEquals(cart.cart['1']['quantity'], 1)
        self.assertEquals(cart.cart['2']['quantity'], 1)
        self.assertEquals(cart.cart['1']['price'], str(spare_part1.purchase_price))
        self.assertEquals(cart.cart['2']['price'], str(spare_part2.purchase_price))

    def test_remove(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        cart.remove(spare_part2)
        self.assertEquals(len(cart.cart), 1)
        self.assertIn(str(spare_part1.id), cart.cart)
        cart.remove(spare_part2)
        self.assertEquals(len(cart.cart), 1)

    def test_len(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2, quantity=3)
        self.assertEquals(len(cart), 4)

    def test_get_total_price(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        total_price = spare_part1.purchase_price + spare_part2.purchase_price
        self.assertAlmostEqual(cart.get_total_price(), Decimal(total_price,), 2)
        cart.add(spare_part2, quantity=2)
        total_price += spare_part2.purchase_price * 2
        self.assertAlmostEqual(cart.get_total_price(), Decimal(total_price), 2)

    def test_clear(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        cart.clear()
        self.assertNotIn(settings.SPARE_PARTS_CART_SESSION_ID, self.request.session)

    def test_iter(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        cart.add(spare_part2)
        self.assertListEqual(
            list(cart),
            [{'spare_part': spare_part1,
              'quantity': 1,
              'price': spare_part1.purchase_price,
              'total_price': spare_part1.purchase_price * 1, },
             {'spare_part': spare_part2,
              'quantity': 2,
              'price': spare_part2.purchase_price,
              'total_price': spare_part2.purchase_price * 2, }
             ]
        )

    def test_get_items_by_supplier(self):
        cart = Cart(self.request)
        spare_part1 = SparePart.objects.get(id=self.spare_part1_id)
        spare_part2 = SparePart.objects.get(id=self.spare_part2_id)
        cart.add(spare_part1)
        cart.add(spare_part2)
        self.assertDictEqual(cart.get_items_by_supplier(),
                             {'Supplier1': [{'spare_part': spare_part1,
                                             'price': spare_part1.purchase_price,
                                             'quantity': 1,
                                             'total_price': spare_part1.purchase_price * 1}],
                              'Supplier2': [{'spare_part': spare_part2,
                                             'price': spare_part2.purchase_price,
                                             'quantity': 1,
                                             'total_price': spare_part2.purchase_price * 1}]

                              })
