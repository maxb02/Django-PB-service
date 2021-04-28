from django.test import SimpleTestCase, TestCase
from sparepart.models import Category, Manufacturer, Supplier


class TestCategory(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='category_name')

    def test_category_str(self):
        category = Category.objects.first()
        self.assertEquals(str(category), 'category_name')

    def test_name_label(self):
        category = Category.objects.first()
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.first()
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

class TestManufacturer(TestCase):

    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name='manufacturer_name')

    def test_name_label(self):
        manufacturer = Manufacturer.objects.first()
        field_label = manufacturer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        manufacturer = Manufacturer.objects.first()
        max_length = manufacturer._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)


class TestSupplier(TestCase):

    @classmethod
    def setUpTestData(cls):
        Supplier.objects.create(name='supplier_name')

    def test_name_label(self):
        supplier = Supplier.objects.first()
        field_label = supplier._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        supplier = Supplier.objects.first()
        max_length = supplier._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)
