from django.test import TestCase
from documents.models import Act, ScopeOfSupply, VisualDefect
from servicecenters.models import ServiceCenter
from users.models import User


class ScopeOfSupplyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ScopeOfSupply.objects.create(item='Charger')

    def test_str_is_item(self):
        obj = ScopeOfSupply.objects.first()
        item_name = str(obj)
        self.assertEquals(item_name, 'Charger')


class VisualDefectTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        VisualDefect.objects.create(defect='Scratch')

    def test_str_is_defect(self):
        obj = VisualDefect.objects.first()
        defect_name = str(obj)
        self.assertEquals(defect_name, 'Scratch')


class ActModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ServiceCenter.objects.create(
            company_name='company',
            manager_name='manager',
            manager_email='test@test.mail',
            country='Ukraine',
            city='Kyiv',
            region='CIS',
            language='ru'
        )

        service_center = ServiceCenter.objects.first()
        User.objects.create(username='test_user',
                            first_name='user_first_name',
                            last_name='user_last_name',
                            email='user@test.mail',
                            service_center=service_center
                            )
        user = User.objects.first()
        Act.objects.create(
            serial_number='YTG912500968002000A6',
            client_name='Bob Mike',
            protocol_number='123',
            received_date='2020-11-12',
            purchase_date='2019-09-05',
            is_presale=False,
            customers_claim='some customers claim',
            identified_malfunction='some identified_malfunction',
            conclusion='some conclusion',
            document_type='warranty_rejection',
            created_by=user)

    def test_querys_number_for_act_creations(self):
        user = User.objects.first()
        with self.assertNumQueries(3):
            Act.objects.create(
                serial_number='YTG912500968002000A6',
                client_name='Bob Mike',
                protocol_number='123',
                received_date='2020-11-12',
                purchase_date='2019-09-05',
                is_presale=False,
                customers_claim='some customers claim',
                identified_malfunction='some identified_malfunction',
                conclusion='some conclusion',
                document_type='warranty_rejection',
                created_by=user)

    def test_str_is_serial_number(self):
        obj = Act.objects.first()
        obj_str = str(obj)
        self.assertEquals(obj_str, 'YTG912500968002000A6')

    def test_number_was_added(self):
        obj = Act.objects.first()
        number = obj.number
        self.assertEquals(number, 'YTG91111')

    def test_get_absolute_url(self):
        obj = Act.objects.first()
        url = obj.get_absolute_url()
        self.assertEquals(url, '/documents/detail/YTG91111')
