# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-27 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import issue.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_serial_number', models.CharField(max_length=20, verbose_name='Device Serial Number')),
                ('filling_date', models.DateTimeField(auto_now_add=True, verbose_name='Fill Date')),
                ('purchase_date', models.DateField(null=True, verbose_name='Purchase Date')),
                ('received_date', models.DateField(verbose_name='Received Date')),
                ('is_presale', models.BooleanField(default=False, verbose_name='Presale')),
                ('battery_serial_number', models.CharField(max_length=20, verbose_name='Battery Serial Number')),
                ('battery_model', models.CharField(max_length=20, verbose_name='Battery Model')),
                ('battery_batch', models.CharField(max_length=20, verbose_name='Battery Batch')),
                ('battery_production_date', models.CharField(max_length=8, verbose_name='Battery Production Date')),
                ('battery_photo', models.ImageField(null=True, upload_to=issue.models.upload_path_handler, verbose_name='Battery photo')),
                ('general_view_photo', models.ImageField(null=True, upload_to=issue.models.upload_path_handler, verbose_name='General view photo')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
            ],
            options={
                'permissions': (('view_battery_issue_list', 'User can view a list of objects'),),
            },
        ),
    ]
