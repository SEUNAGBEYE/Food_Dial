# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
import time
from django.shortcuts import render, redirect
from django.conf.urls import url
from django.http import HttpResponse
from Homepage.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# from Homepage.cart import Cart
from django.contrib.auth import authenticate, login , logout


from Homepage.models import UserAccount, Product, Orders


# import numpy as np
import cv2
# cap = cv2.VideoCapture('001-how-the-course-is-structured.mp4') Used for playing video
# cap = cv2.VideoCapture(0 + cv::CAP_FFMPEG)

def start_video_call(request):
	cap = cv2.VideoCapture(0)
	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    # ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,500) 
	    # ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
	    # Our operations on the frame come here
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    # Display the resulting frame
	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	return index(request)


# Create your views here.

def index(request):

	context = {}
	reg_form = RegistrationForm()
	login_form = LoginForm()
	context['reg_form'] = reg_form
	context['login_form'] = login_form
	foodToPurchase = Product.objects.filter(is_available = True)
	foods = foodToPurchase
	timer1 = time.localtime()
	timer = timer1[3]+1 >= 9
	# print timer1[3]

	context['foods'] = foods
	# else:
	context['timer'] = timer

	
	return render(request, 'Homepage/index1.html', context)

	# REGISTER VIEW CONTROL



def registrationView(request):

	context = {}
	reg_form = RegistrationForm()
	context['reg_form'] = reg_form

	if request.method == 'POST':
		# print 'hello post'
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

				#create user object for new user
				user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'])
				user.set_password(rp['password'])
				user.save()
				# print user

				#create a useraccount for the newly created user
				useraccount = UserAccount.objects.create(user = user)

				if user:
					# recipent = ['ottimothy@gmail.com']
					# sender = ['agbeyeseun1@gmail.com']
					# send_mail('Hi your account has been succesfully created', 'your account has been succesfully created',sender, recipent )
					messages.success(request, 'our account details have been saved')
					print('new user created %s' %(user.username))
					return redirect(reverse('Homepage:index'))
				else:
					messages.warning(request, 'Sorry something went wrong while savings your records, please try again.')
			else:
				# print 'form is not valid'
				# print request.POST
				# print user_mgr
				context['reg_form'] = RegistrationForm(data = request.POST)
	
	return render(request, 'Homepage/index1.html', context)


def loginView(request):
	context = {}
	login_form = LoginForm()
	auth_user = False
	context['login_form'] = login_form
	if request.method == 'POST':
		login_form = LoginForm(data = request.POST)
		rp = request.POST
		

		# checks if user mail in database
		if User.objects.filter(email = rp['email']).exists():
			username = User.objects.get(email = rp['email']).username
			auth_user = authenticate(username = username, password = rp['password'])

			if auth_user:
				logged_in_user = login(request, auth_user)
				print('You have been logged in!')
				return redirect(reverse('Homepage:index'))

			else:
				context['login_form'] = login_form
				messages.error(request, 'Sorry your email or password is Incorrect!')
				return redirect(reverse('Homepage:index'))
		else:
			messages.error(request, 'Sorry this email address does not exist')
	

			context['login_form'] = login_form

			# return render(request, 'Homepage/index.html', context)
			return redirect(reverse('Homepage:index'))
	context['login_form'] = login_form
	return redirect(reverse('Homepage:index'))

def logoutView(request):
	logout_user = logout(request)
	return redirect(reverse('Homepage:index'))

def orderView(request, food_id):

	
	food = Product.objects.get(id = food_id)
	if(Orders.objects.filter(food_name = food).exists()):

		order = Orders.objects.filter(food_name = food).first()
		useraccount = UserAccount.objects.filter(user = request.user).first()

		if(useraccount.order == None):
			useraccount = UserAccount.objects.filter(user = request.user).first()
			order.user = order.user + ',' + ' ' + request.user.username
			order.quantity += 1
			# useraccount.order = order
			# print useraccount.order
			order.save()

			return redirect(reverse('Homepage:index'))
		else:
			messages.info(request, 'you have choosen and cannot choose again')

			return redirect(reverse('Homepage:index'))
	else:
			useraccount = UserAccount.objects.filter(user = request.user).first()

			if(useraccount.order == None):
				order = Orders.objects.create(food_name = food, user = request.user.username, quantity = +1) 
				useraccount = UserAccount.objects.filter(user = request.user).first()
				useraccount.order = order
				useraccount.save()
			
				# print messages.info(request, 'you have choosen ')
				# print 'hi'
				return redirect(reverse('Homepage:index'))
			else:
				# print messages.info(request, 'you have choosen and cannot choose again')
				# print 'hi you choose'
				return redirect(reverse('Homepage:index'))
	return redirect(reverse('Homepage:index'))