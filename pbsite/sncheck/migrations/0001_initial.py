# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedDeviceRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_region', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmailForNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SerialNumberCheckJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, verbose_name='Serial Number')),
                ('is_valid', models.NullBooleanField(verbose_name='SN is valid')),
                ('is_region_match', models.NullBooleanField(verbose_name='Region Match')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
