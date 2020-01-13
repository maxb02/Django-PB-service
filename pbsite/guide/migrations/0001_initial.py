# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-12-04 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('technicalguides', '0002_auto_20180614_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='technicalguides.Device')),
                ('group', models.ManyToManyField(related_name='guides', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Guide')),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Step'),
        ),
        migrations.AddField(
            model_name='link',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Step'),
        ),
        migrations.AddField(
            model_name='image',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Step'),
        ),
        migrations.AddField(
            model_name='file',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Step'),
        ),
    ]
