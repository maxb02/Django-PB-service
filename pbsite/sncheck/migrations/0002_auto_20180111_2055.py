# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sncheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email_list',
            new_name='EmailForNotifications',
        ),
    ]
