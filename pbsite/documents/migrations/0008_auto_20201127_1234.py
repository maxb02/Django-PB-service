# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-11-27 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20190807_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='act',
            options={'ordering': ['-filling_date'], 'permissions': (('accept_or_decline_acts', 'User can accept or decline acts'),)},
        ),
    ]
