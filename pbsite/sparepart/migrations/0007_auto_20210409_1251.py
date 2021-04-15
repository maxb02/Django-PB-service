# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-04-09 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sparepart', '0006_auto_20200715_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spare_parts', to='sparepart.Category', verbose_name='Category'),
        ),
    ]