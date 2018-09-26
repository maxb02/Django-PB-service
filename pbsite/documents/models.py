from django.db import models

class Act(models.Model):
    serial_number = models.CharField(max_length=50, verbose_name ='Serial Number')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name ='User Name')
    filling_date = models.DateTimeField(blank=True, auto_now_add=True)
    purchase_date = models.DateTimeField(verbose_name ='Purchase Date')
    received_date = models.DateTimeField(verbose_name ='Received Date')
    conclusion_date = models.DateTimeField(null=True, verbose_name='Conclusion Date')
    is_presale = models.BooleanField(verbose_name='It is presale')
    photo = models.ImageField(null=True, blank=True)
    client_name = models.CharField(max_length=50, verbose_name ='Client Name')
    seller_name= models.CharField(max_length=50, verbose_name='Seller Name')
    type = models.CharField(max_length=100, verbose_name='Type',choices=(
                                                        ('MBD', 'Money Back Document'),
                                                        ('OOW', 'Out of Warranty'),
                                                        ('NFF', 'No Fault Found'),
                                                        ('RM', 'Region Mismatch')
                                                    ))
    status = models.CharField(max_length=50, verbose_name='Status',choices=(
                                                        ('in_process', 'In Process'),
                                                        ('confirmed', 'Confirmed'),
                                                        ('rejected', 'Rejected'),
                                                    ))
