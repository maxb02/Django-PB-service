from django.db import models
from device.models import Device


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
    device = models.ForeignKey(Device, related_name='spare_part', verbose_name='Device')
    category = models.ForeignKey(Category, related_name='category', verbose_name='Category')
    image = models.ImageField(upload_to='spareparts', verbose_name='Photo')
    weight = models.PositiveSmallIntegerField(verbose_name='Weight grams')
    size = models.CharField(max_length=25, verbose_name='Size, millimeters')
    part_number = models.CharField(max_length=50, verbose_name='Part Number')
    description = models.TextField(verbose_name='Short description')
    comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, related_name='spare_part', verbose_name='Supplier')
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer', verbose_name='Manufacturer')
    purchase_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Purchase price, $')

    def __str__(self):
        return '{} {}'.format(self.device, self.name)
