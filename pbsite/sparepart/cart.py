from decimal import Decimal
from collections import defaultdict
from django.conf import settings
from .models import SparePart


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SPARE_PARTS_CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.SPARE_PARTS_CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, spare_part, quantity=1, update_quantity=False):
        spare_part_id = str(spare_part.id)
        if spare_part_id not in self.cart:
            self.cart[spare_part_id] = {
                'quantity': 0,
                'price': str(spare_part.purchase_price)
            }
        if update_quantity:
            self.cart[spare_part_id]['quantity'] = quantity
        else:
            self.cart[spare_part_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, spare_part):
        spare_part_id = str(spare_part.id)
        if spare_part_id in self.cart:
            del self.cart[spare_part_id]
            self.save()


    def __iter__(self):

        spare_part_ids = self.cart.keys()
        spare_parts = SparePart.objects.filter(id__in=spare_part_ids)

        cart = self.cart.copy()
        for spare_part in spare_parts:
            cart[str(spare_part.id)]['spare_part'] = spare_part

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.SPARE_PARTS_CART_SESSION_ID]
        self.save()

    def get_items_by_supplier(self):
        d = defaultdict(list)
        for item in self:
            supplier_name = item['spare_part'].supplier.name
            d[supplier_name].append(item)
        return dict(d)
