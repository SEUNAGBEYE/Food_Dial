# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0008_auto_20170516_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
