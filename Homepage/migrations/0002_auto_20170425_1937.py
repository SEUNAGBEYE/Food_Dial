# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductTable',
            new_name='Products',
        ),
        migrations.AlterModelOptions(
            name='foodcategories',
            options={'verbose_name_plural': 'FoodCategories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
    ]