# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 19:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
        ('sncheck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serialnumbercheckjournal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Name'),
        ),
        migrations.AddField(
            model_name='emailfornotifications',
            name='user_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='alloweddeviceregion',
            name='user_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
