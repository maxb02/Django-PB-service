# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-01-19 09:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0013_auto_20210116_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='ean',
            field=models.CharField(default='000', help_text='European Article Number', max_length=13, validators=[django.core.validators.RegexValidator(code='nomatch', message='EAN-13 length has to be 13', regex='^.{13}$')], verbose_name='EAN-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sku',
            name='model_name',
            field=models.CharField(default='---', max_length=25),
            preserve_default=False,
        ),
    ]
