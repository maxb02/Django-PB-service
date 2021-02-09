# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-02-08 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicecenters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecenter',
            name='language',
            field=models.CharField(choices=[('ru', 'Russian'), ('en', 'English'), ('ua', 'Ukrainian')], max_length=50),
        ),
    ]