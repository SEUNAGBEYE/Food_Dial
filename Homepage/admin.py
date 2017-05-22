# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Homepage.models import FoodCategories, Product, UserAccount, Address, Wallet, WeekDay

# Register your models here.
admin.site.register(FoodCategories)
admin.site.register(Product)
admin.site.register(UserAccount)
admin.site.register(Address)
admin.site.register(Wallet)
admin.site.register(WeekDay)
# admin.site.register(WeekDay)
# admin.site.register(OrderDetail)