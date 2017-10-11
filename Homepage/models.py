# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from Homepage.model_field_choices import STATUS, GENDER, WEEKDAY



# Create your models here.

class FoodCategories(models.Model):
	name = models.CharField(max_length = 128)

	class Meta:
		verbose_name_plural = 'FoodCategories'

	def __str__(self):
		return self.name
			

class Product(models.Model):
	food_categories = models.ForeignKey('FoodCategories')
	name = models.CharField(max_length = 128)
	image = models.FileField(upload_to ='media/' )
	description = models.TextField(help_text = 'Write about the food here', blank = True, null = True )
	price = models.FloatField(default = 0)
	quantity = models.IntegerField(default=0)
	is_available = models.BooleanField(default = False)
	days_available = models.ManyToManyField('Weekday')

	class Meta:
		verbose_name_plural = 'Products'
		ordering = ['name']

	def __str__(self):
		return self.name

	def totalAmount(self):
		return self.price*self.quantity




	class Meta:
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.name


class WeekDay(models.Model):
	weekday 	=	models.CharField(max_length = 20, choices = WEEKDAY)

	def __str__(self):
		return self.weekday


class UserAccount(models.Model):
	user = models.OneToOneField(User)
	gender = models.CharField(max_length = 10, choices = GENDER, null = True, blank = True)
	phone = models.IntegerField(default = 0)
	order = models.OneToOneField('Orders', null = True, blank = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.user.username

class Orders(models.Model):
	user = models.TextField();
	food_name = models.ForeignKey('Product')
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.food_name.name

	class Meta:
		verbose_name_plural = 'Orders'
			