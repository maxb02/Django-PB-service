from django.db import models
from django.conf import settings
import datetime

def upload_path_handler(self, filename):
    return "document/{serial_number}/{date}/{file}".format(serial_number=self.serial_number,
                                                         date=datetime.datetime.now().strftime ("%Y.%m.%d"),
                                                         file=filename)

class Act(models.Model):
    serial_number = models.CharField(max_length=20, verbose_name ='Serial Number')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,related_name='created_by', verbose_name ='User Name')
    accepted_or_declined_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,related_name='accepted_or_declined_by', verbose_name ='Accepted or declined by')
    filling_date = models.DateTimeField( auto_now_add=True)
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
    status = models.CharField(max_length=50, verbose_name='Status', default='in_process',choices=(
                                                        ('in_process', 'In Process'),
                                                        ('confirmed', 'Confirmed'),
                                                        ('rejected', 'Rejected'),
                                                    ))

    comment_of_engineer = models.TextField(max_length=140, null=True, blank=True, verbose_name='Comment of Engineer')
    comment_of_manager = models.TextField(max_length=140, null=True, blank=True,verbose_name='Comment of Manager')

    def __str__(self):
        return self.serial_number


class SerialNumberPrefix(models.Model):
    model = models.CharField(max_length=50, verbose_name='Device name')
    prefix= models.CharField(max_length=3, verbose_name='Serial Number Prefix')

    def __str__(self):
        return self.prefix

