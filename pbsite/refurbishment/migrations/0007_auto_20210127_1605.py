# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-27 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refurbishment', '0006_auto_20210112_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='sku_suffix',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Suffix for base SKU'),
        ),
    ]