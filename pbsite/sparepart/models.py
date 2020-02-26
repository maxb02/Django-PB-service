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
    name = models.CharField(max_length=50)
    device = models.ForeignKey(Device, related_name='spare_part')
    category = models.ForeignKey(Category, related_name='category', null=True)
    image = models.ImageField(upload_to='spareparts')
    weight = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=25)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    comment = models.TextField()
    supplier = models.ForeignKey(Supplier, related_name='spare_part')
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer')
    purchase_price = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return '{} {}'.format(self.device, self.name)
