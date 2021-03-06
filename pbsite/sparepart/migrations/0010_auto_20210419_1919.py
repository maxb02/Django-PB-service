# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-04-19 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0009_auto_20210419_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersupplier',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Invoice Number'),
        ),
        migrations.AlterField(
            model_name='ordersupplier',
            name='post_service',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Delivery Service Name'),
        ),
        migrations.AlterField(
            model_name='ordersupplier',
            name='track_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Track Number'),
        ),
    ]
