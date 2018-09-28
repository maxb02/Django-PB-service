from django.db import models
from django.conf import settings
import datetime

def upload_path_handler(self, filename):
    return "document/{serial_number}/{date}/{file}".format(serial_number=self.serial_number,
                                                         date=datetime.datetime.now().strftime ("%Y.%m.%d"),
                                                         file=filename)

class Act(models.Model):
    serial_number = models.CharField(max_length=20, verbose_name ='Serial Number')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name ='User Name')
    filling_date = models.DateTimeField(blank=True, auto_now_add=True)
    purchase_date = models.DateField(verbose_name ='Purchase Date')
    received_date = models.DateField(verbose_name ='Received Date')
    conclusion_date = models.DateTimeField(null=True, blank=True, verbose_name='Conclusion Date')
    is_presale = models.BooleanField(verbose_name='It is presale')

    customers_claim = models.CharField(max_length = 50, verbose_name ='Customers Claim')
    identified_malfunction = models.CharField(max_length = 50, verbose_name ='Identified Malfunction')

    warranty_card_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler, verbose_name='Photo of warranty card or receipt')
    receipt_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler,verbose_name='Photo of warranty card or receipt')
    screen_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler, verbose_name='Photo of screen')
    defect_photo = models.ImageField(null=True, blank=True, upload_to=upload_path_handler, verbose_name='Photo of defect')


    client_name = models.CharField(max_length=50, verbose_name ='Client Name')
    seller_name= models.CharField(max_length=50, verbose_name='Seller Name')
    document_type = models.CharField(max_length=100, verbose_name='Type',choices=(
                                                        ('money_back_document', 'Money Back Document'),
                                                        ('out_of_warranty', 'Out of Warranty'),
                                                        ('no_fault_found', 'No Fault Found'),
                                                        ('region_mismatch', 'Region Mismatch')
                                                    ))
    status = models.CharField(max_length=50, verbose_name='Status',choices=(
                                                        ('in_process', 'In Process'),
                                                        ('confirmed', 'Confirmed'),
                                                        ('rejected', 'Rejected'),
                                                    ))

    comment_of_engineer =



    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

