# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-14 10:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('alert alert-primary', 'primary'), ('alert alert-success', 'success'), ('alert alert-danger', 'danger'), ('alert alert-warning', 'warning'), ('alert alert-info', 'info'), ('alert alert-light', 'light'), ('alert alert-dark', 'dark')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contents')),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('group', models.ManyToManyField(to='auth.Group')),
            ],
        ),
    ]
