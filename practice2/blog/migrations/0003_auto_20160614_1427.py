# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160614_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
