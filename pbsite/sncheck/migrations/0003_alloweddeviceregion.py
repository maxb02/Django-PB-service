# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-25 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('sncheck', '0002_auto_20180111_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedDeviceRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_region', models.CharField(max_length=200)),
                ('user_region', models.ManyToManyField(to='auth.Group')),
            ],
        ),
    ]
