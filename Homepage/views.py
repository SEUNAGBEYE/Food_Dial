# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponse
from Homepage.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login , logout


from Homepage.models import UserAccount, Product



# Create your views here.

def index(request):
	context = {}
	reg_form = RegistrationForm()
	login_form = LoginForm()
	context['reg_form'] = reg_form
	context['login_form'] = login_form
	# return HttpResponse('Welcome to Food Dial')
	# return render(request, 'Homepage/index.html')
	# meals_for_the_day   =   Product.objects.filter(days_available__in = "")
	foodToPurchase = Product.objects.filter(is_available = True)
	foods = foodToPurchase
	# food_name = foodToPurchase.name
	# food_image = foodToPurchase.image.url
	# food_price = foodToPurchase.price
	# context['food_name'] = food_name
	# context['food_image'] = food_image
	# context['food_price'] = food_price
	context['foods'] = foods

	# foodToPurchase2 = Product.objects.get(id = 2)
	# food_name2 = foodToPurchase2.name
	# food_image2 = foodToPurchase2.image.url
	# food_price2 = foodToPurchase2.price
	# context['food_name2'] = food_name2
	# context['food_image2'] = food_image2
	# context['food_price2'] = food_price2
	return render(request, 'Homepage/index1.html', context)

	# REGISTER VIEW CONTROL


# def registrationView(request):

# 	context = {}
# 	reg_form = RegistrationForm()
# 	context['reg_form'] = reg_form

# 	if request.method == 'POST':
# 		user_reg_form = RegistrationForm(data = request.POST)

# 		rp = request.POST

# 		if User.objects.filter(email = rp['email']).exists():
# 			messages.info(request, 'Sorry this user email is alredy used')
# 			return redirect(reverse('Homepage:index'))

# 		if User.objects.filter(username = rp['username']).exists():
# 			messages.info(request, 'Sorry this user email is already used')
# 			return redirect(reverse('Homepage:index'))


# 		else:
# 			if user_reg_form.is_valid():
# 				# user_reg_form.save()

# 				#create user object for new user
# 				user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'])
# 				user.set_password(rp['password'])
# 				user.save()

# 				#create a useraccount for the newly created user
# 				useraccount = UserAccount.objects.create(user = user)

# 				if user:
# 					# recipent = ['ottimothy@gmail.com']
# 					# sender = ['agbeyeseun1@gmail.com']
# 					# send_mail('Hi your account has been succesfully created', 'your account has been succesfully created',sender, recipent )
# 					messages.success(request, 'our account details have been saved')
# 					print 'new user created %s' %(user.username)
# 					return redirect(reverse('Homepage:index'))
# 				else:
# 					messages.warning(request, 'Sorry something went wrong while savings your records, please try again.')
# 			else:
# 				print 'form is not valid'
# 				# print request.POST
# 				# print user_mgr
# 				context['reg_form'] = RegistrationForm(data = request.POST)
	
# 	return render(request, 'Homepage/index.html', context)


# def loginView(request):
# 	context = {}
# 	login_form = LoginForm()
# 	auth_user = False
# 	context['login_form'] = login_form
# 	if request.method == 'POST':
# 		login_form = LoginForm(data = request.POST)
# 		rp = request.POST
# 		print 'its a post'

# 		# checks if user mail in database
# 		if User.objects.filter(email = rp['email']).exists():
# 			username = User.objects.get(email = rp['email']).username
# 			auth_user = authenticate(username = username, password = rp['password'])

# 			if auth_user:
# 				logged_in_user = login(request, auth_user)
# 				print('You have been logged in!')
# 				return render(request, 'Homepage/admin.html', {'username':username})

# 			else:
# 				context['login_form'] = login_form
# 				messages.error(request, 'Sorry your email or password is Incorrect!')
# 				return render(request, 'Homepage/index.html', context)
# 		else:
# 			messages.error(request, 'Sorry this email address does not exist')
	

# 			context['login_form'] = login_form

# 			return render(request, 'Homepage/index.html', context)
# 	# return HttpResponse('We are at the Login page <a href="/register">Register here</a>')
# 	context['login_form'] = login_form
# 	return render(request, 'Homepage/index.html', context)

# def about(request):
# 	return HttpResponse('This is all about Us!!')

def registrationView(request):

	context = {}
	reg_form = RegistrationForm()
	context['reg_form'] = reg_form

	if request.method == 'POST':
		user_reg_form = RegistrationForm(data = request.POST)

		rp = request.POST

		if User.objects.filter(email = rp['email']).exists():
			messages.info(request, 'Sorry this user email is alredy used')
			return redirect(reverse('Homepage:index'))

		if User.objects.filter(username = rp['username']).exists():
			messages.info(request, 'Sorry this user email is already used')
			return redirect(reverse('Homepage:index'))


		else:
			if user_reg_form.is_valid():
				# user_reg_form.save()

				#create user object for new user
				user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'])
				user.set_password(rp['password'])
				user.save()

				#create a useraccount for the newly created user
				useraccount = UserAccount.objects.create(user = user)

				if user:
					# recipent = ['ottimothy@gmail.com']
					# sender = ['agbeyeseun1@gmail.com']
					# send_mail('Hi your account has been succesfully created', 'your account has been succesfully created',sender, recipent )
					messages.success(request, 'our account details have been saved')
					print 'new user created %s' %(user.username)
					return redirect(reverse('Homepage:index'))
				else:
					messages.warning(request, 'Sorry something went wrong while savings your records, please try again.')
			else:
				print 'form is not valid'
				# print request.POST
				# print user_mgr
				context['reg_form'] = RegistrationForm(data = request.POST)
	
	return render(request, 'Homepage/index.html', context)


def loginView(request):
	context = {}
	login_form = LoginForm()
	auth_user = False
	context['login_form'] = login_form
	if request.method == 'POST':
		login_form = LoginForm(data = request.POST)
		rp = request.POST
		print 'its a post'

		# checks if user mail in database
		if User.objects.filter(email = rp['email']).exists():
			username = User.objects.get(email = rp['email']).username
			auth_user = authenticate(username = username, password = rp['password'])

			if auth_user:
				logged_in_user = login(request, auth_user)
				print('You have been logged in!')
				return render(request, 'Homepage/admin1.html', {'username':username})

			else:
				context['login_form'] = login_form
				messages.error(request, 'Sorry your email or password is Incorrect!')
				return render(request, 'Homepage/index.html', context)
		else:
			messages.error(request, 'Sorry this email address does not exist')
	

			context['login_form'] = login_form

			return render(request, 'Homepage/index.html', context)
	# return HttpResponse('We are at the Login page <a href="/register">Register here</a>')
	context['login_form'] = login_form
	return render(request, 'Homepage/index.html', context)

def about(request):
	return HttpResponse('This is all about Us!!')

def productView(request):
	return render(request, 'Homepage/product.html')

def baseView(request):
	context = {}
	reg_form = RegistrationForm()
	login_form = LoginForm()
	context['reg_form'] = reg_form
	context['login_form'] = login_form
	# return HttpResponse('Welcome to Food Dial')
	# return render(request, 'Homepage/index.html')
	return render(request, 'Homepage/base.html', context)
# def cartView(request):
# 	return render(request, 'Homepage/shopping-cart.html')

def checkoutView(request):
	return render(request, 'Homepage/checkout.html')

def successView(request):
	# return render(request, "Homepage/base.html", )
	return render(request, 'Homepage/success.html')




# def addToCart(request, food_id):
# 	context  =   {}
# 	foodToPurchase = Product.objects.get(id = food_id)
# 	if request.user.is_authenticated():
# 		OrderDetail.objects.create(user = request.user, product = foodToPurchase)
# 	else:
# 		annonymous_user =  User.objects.create(first_name = "annonymous", email = "email@gmail.com")
# 		OrderDetail.objects.create(user = annonymous_user, product = foodToPurchase, is_annonymous = True)

# 	context['food_selected']= foodToPurchase
# 	return render(request, 'shopping-cart.html', context)

def addToCartView(request, id):
	context = {}
	foodToPurchase = Product.objects.get(id = Product.objects.id )
	food_name = foodToPurchase.name
	food_image = foodToPurchase.image.url
	food_price = foodToPurchase.price
	context['food_name'] = food_name
	context['food_image'] = food_image
	context['food_price'] = food_price

	foodToPurchase6 = Product.objects.get(id = 6)
	food_name6 = foodToPurchase6.name
	food_image6 = foodToPurchase6.image.url
	food_price6 = foodToPurchase6.price
	context['food_name6'] = food_name6
	context['food_image6'] = food_image6
	context['food_price6'] = food_price6


	return render(request, 'Homepage/shopping-cart.html', context)







	
	

	
