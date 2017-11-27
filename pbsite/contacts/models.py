from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    country = models.ForeignKey(Country, null= True, blank= True)

    def __str__(self):
        return self.number

class Email(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

class Link(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

