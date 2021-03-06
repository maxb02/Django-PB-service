# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-12-03 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Condition nmae')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Defect name')),
            ],
        ),
        migrations.CreateModel(
            name='Refurbishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Refurbishment name')),
            ],
        ),
        migrations.CreateModel(
            name='RefurbishmentDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_serial_number', models.CharField(max_length=20, unique=True, verbose_name='Old Serial Number')),
                ('new_serial_number', models.CharField(max_length=20, unique=True, verbose_name='New Serial Number')),
                ('notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Notes')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of update')),
                ('was_returned', models.BooleanField(default=False, verbose_name='Device was returned')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refurbishment.Condition', verbose_name='Refurbishment Device Condition')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refurbishment_device_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By User')),
                ('defect', models.ManyToManyField(to='refurbishment.Defect', verbose_name='Defect')),
                ('refurbishment', models.ManyToManyField(to='refurbishment.Refurbishment', verbose_name='Refurbishment')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refurbishment_device_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated By User')),
            ],
            options={
                'permissions': (('view_refurbishment_device_list', 'User can view a list of Refurbishment Devices'),),
            },
        ),
    ]
