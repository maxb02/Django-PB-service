# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-02-26 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0002_auto_20200226_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='spareparts')),
                ('weight', models.PositiveSmallIntegerField()),
                ('size', models.CharField(max_length=25)),
                ('sku', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('comment', models.TextField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sparepart.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='sparepart',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sparepart.Supplier'),
        ),
    ]