# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-16 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0011_auto_20210113_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
