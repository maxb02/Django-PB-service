# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-19 09:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import issue.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0002_auto_20200421_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayLineIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_serial_number', models.CharField(max_length=20, unique=True, verbose_name='Device Serial Number')),
                ('filling_date', models.DateTimeField(auto_now_add=True, verbose_name='Fill Date')),
                ('purchase_date', models.DateField(null=True, verbose_name='Purchase Date')),
                ('received_date', models.DateField(verbose_name='Received Date')),
                ('is_presale', models.BooleanField(default=False, verbose_name='Presale')),
                ('display_photo', models.ImageField(upload_to=issue.models.display_line_upload_path_handler, verbose_name='Display photo')),
                ('display_label_photo', models.ImageField(upload_to=issue.models.display_line_upload_path_handler, verbose_name='Display label photo')),
                ('warranty_card_photo', models.ImageField(blank=True, null=True, upload_to=issue.models.display_line_upload_path_handler, verbose_name='Photo of warranty card')),
                ('receipt_photo', models.ImageField(blank=True, null=True, upload_to=issue.models.display_line_upload_path_handler, verbose_name='Photo of receipt')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='display_line_issues', to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
            ],
        ),
    ]
