# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-27 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_act_compensation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='compensation_status',
            field=models.CharField(choices=[('nc_nr', 'NOT compensated/NOT returned'), ('nc_r', 'NOT compensated/Returned'), ('c_nr', 'Compensated/NOT returned'), ('c_n', 'Compensated/Returned')], default='nc_nr', max_length=5, null=True),
        ),
    ]