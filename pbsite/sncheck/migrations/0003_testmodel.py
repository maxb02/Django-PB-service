# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-20 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sncheck', '0002_auto_20180612_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asd', models.CharField(max_length=50, verbose_name='Serial Number')),
            ],
        ),
    ]
