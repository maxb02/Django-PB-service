# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-09-21 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0003_displaylineissue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='displaylineissue',
            options={'permissions': (('view_display_line_issue_list', 'User can view a list of objects'),)},
        ),
    ]
