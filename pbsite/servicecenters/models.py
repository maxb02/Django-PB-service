from django.db import models


class ServiceCenter(models.Model):
    company_name = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    manager_email = models.EmailField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=50, choices=(
                                                        ('WordWide', 'WordWide'),
                                                        ('RU', 'RU'),
                                                        ('CIS', 'CIS'),
                                                    ))
    language = models.CharField(max_length=50, choices=(
                                                        ('ru', 'Russian'),
                                                        ('en', 'English'),

    ))

    def __str__(self):
        return '{}, {}, {}'.format(self.company_name, self.country, self.city)