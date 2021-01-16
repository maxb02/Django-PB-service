# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-12 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refurbishment', '0004_auto_20210112_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='label_date_field_name',
            field=models.CharField(choices=[('prd', 'Production date'), ('ref', 'Refurbish date')], max_length=5),
        ),
    ]