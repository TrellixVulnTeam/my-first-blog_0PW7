# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160614_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
