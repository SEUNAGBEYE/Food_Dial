# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Homepage.models import FoodCategories, Product, UserAccount, WeekDay, Orders

# Register your models here.
admin.site.register(FoodCategories)
admin.site.register(Product)

admin.site.register(WeekDay)

admin.site.register(Orders)

admin.site.register(UserAccount)