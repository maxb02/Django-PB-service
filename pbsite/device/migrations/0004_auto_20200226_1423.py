# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-02-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20200226_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial_number_prefix',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]