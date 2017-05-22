# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from model_field_choices import STATUS, GENDER, WEEKDAY



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



# class Product(models.Model):
# 	food_categories = models.ForeignKey('FoodCategories')
# 	name 			= models.CharField(max_length = 128)
# 	image          	=    models.FileField(upload_to ='media/' )
# 	price			= models.FloatField()
# 	description    	=    models.TextField(help_text = 'Write about the food here', blank = True, null = True )
# 	is_available   	=    models.BooleanField(default = True)
# 	days_available 	=	models.ManyToManyField('WeekDay')


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
	marital_status = models.CharField(max_length = 10, choices = STATUS, null = True, blank = True)
	phone = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.username

class Address(models.Model):
	user_address = models.OneToOneField('UserAccount')
	house_address = models.TextField()
	lga = models.CharField(max_length = 20)
	state = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)

	class Meta:
		verbose_name_plural = 'Address'

	def __str__(self):
		return self.house_address

class Wallet(models.Model):
	user_wallet = models.OneToOneField('UserAccount')
	balance = models.FloatField(max_length=20)
	# update_balance= models.FloatField(max_length=20, blank=True, null = True)

	def get_balance(self):
		print self.balance

	def update_balance(self,new_balance):
		self.balance+=new_balance
		return self.balance

	def withdraw(self, amount):
		self.balance-=new_balancee
		return self.balance

	def __str__(self):
		return self.user_wallet.user.username + ' Wallet'

class Checkout(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 20)
	company_name = models.CharField(max_length = 20, blank=True, null = True)
	address1 = models.CharField(max_length = 20)
	address2 = models.CharField(max_length = 20, blank=True, null = True)
	city = models.CharField(max_length = 20)
	order_comment = models.CharField(max_length = 20, blank=True, null = True)	
		

# class OrderDetail(models.Model):
# 	user 			= models.OneToOneField(User)
# 	product 		= models.ForeignKey(Product)
# 	date 			= models.DateTimeField(auto_now_add=True, auto_now=False)
# 	is_completed	= models.BooleanField(default=False)
# 	is_anonymous	= models.BooleanField(default=False)

# 	def __str__(self):
# 		return "%s | %s" %(self.user.username, self.product.name)