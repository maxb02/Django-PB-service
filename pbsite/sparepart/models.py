from django.db import models
from django.shortcuts import reverse
from device.models import Device
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SparePart(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of spare part')
    device = models.ManyToManyField(Device, related_name='spare_parts', verbose_name='Device')
    category = models.ForeignKey(Category, related_name='spare_parts', verbose_name='Category', null=True)
    image = models.ImageField(upload_to='spareparts', verbose_name='Photo', blank=True)
    weight = models.PositiveSmallIntegerField(verbose_name='Weight grams')
    size = models.CharField(max_length=25, verbose_name='Size, millimeters')
    sku = models.CharField(max_length=50, verbose_name='Part Number')
    description = models.TextField(verbose_name='Short description')
    comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, related_name='spare_part', verbose_name='Supplier')
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer', verbose_name='Manufacturer')
    purchase_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Purchase price, $')

    def __str__(self):
        return '{} | {}'.format(self.name, self.sku)

    def get_absolute_url(self):
        return reverse('spare_part_detail_url', kwargs={'pk': self.pk})


class Order(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='orders',
                                   verbose_name=_('orders'))
    created_date = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=50, verbose_name=_('Order destination'))

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_total_cost for item in self.orders_supplier.all())


class OrderSupplier(models.Model):
    STATUS_CHOICES = (
        ('in_process', _('In Process')),
        ('ordered', _('Ordered')),
        ('shipped', _('Shipped')),
        ('received', _('Received')),
    )

    order = models.ForeignKey(Order,
                              related_name='orders_supplier',
                              on_delete=models.CASCADE,)
    supplier = models.ForeignKey(Supplier,
                                 verbose_name='orders_supplier',
                                 on_delete=models.DO_NOTHING)
    invoice_number = models.CharField(max_length=30, verbose_name=_('Invoice Number'), null=True, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.CharField(max_length=20, default='in_process', choices=STATUS_CHOICES)
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))
    post_service = models.CharField(max_length=50, verbose_name=_('Delivery Service Name'), null=True, blank=True)
    track_number = models.CharField(max_length=50, verbose_name=_('Track Number'), null=True, blank=True)
    estimated_delivery_date = models.DateField(blank=True, null=True)
    delivered_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Order Supplier {}, {}'.format(self.supplier, self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def get_excel_file_url(self):
        return reverse('order_file', kwargs={'pk': self.pk})


class OrderItem(models.Model):
    order_supplier = models.ForeignKey(OrderSupplier,
                                       related_name='order_items',
                                       on_delete=models.CASCADE,
                                       )
    spare_part = models.ForeignKey(SparePart,
                                   related_name='order_items',
                                   on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return 'Order Item {}, {} pcs'.format(self.spare_part, self.quantity)

    def get_cost(self):
        return self.price * self.quantity


