# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0010_auto_20201225_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='device.Factory'),
        ),
    ]
