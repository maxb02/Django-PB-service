# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-08-07 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20190729_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='customers_claim',
            field=models.CharField(max_length=300, verbose_name='Customer Claim'),
        ),
    ]
