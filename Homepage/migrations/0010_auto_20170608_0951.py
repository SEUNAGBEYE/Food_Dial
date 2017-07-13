# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 08:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Homepage', '0009_auto_20170516_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('food_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_address',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='user_wallet',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]