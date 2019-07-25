# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20181119_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='number',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Document Number'),
        ),
        migrations.AlterField(
            model_name='act',
            name='comment_of_engineer',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Comments (for PocketBook)'),
        ),
        migrations.AlterField(
            model_name='act',
            name='comment_of_manager',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Comment of Manager'),
        ),
        migrations.AlterField(
            model_name='act',
            name='document_type',
            field=models.CharField(choices=[('warranty_rejection', 'Statement of manufacturer warranty rejection'), ('technical_inspection', 'Statement of manufacturer technical inspection'), ('defect_acceptance', 'Statement of  manufacturer defect acceptance'), ('discount_voucher_50', 'Statement of  manufacturer defect acceptance and 50% discount voucher'), ('discount_voucher_20', 'Statement of  manufacturer defect acceptance and 20% discount voucher')], max_length=100, verbose_name='Document type'),
        ),
        migrations.AlterField(
            model_name='act',
            name='filling_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fill Date'),
        ),
        migrations.AlterField(
            model_name='act',
            name='serial_number',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Serial Number'),
        ),
    ]
