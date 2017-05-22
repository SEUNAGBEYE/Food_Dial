from django import forms
from Homepage.models import UserAccount
from django.contrib.auth.models import User



class UserAccount(forms.ModelForm):
	gender = forms.CharField(max_length = 128, widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Gender', 'required': 'required'}))
	marital_status = forms.CharField(max_length = 128, widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Marital Status', 'required':'required'}))
	phone = forms.CharField(max_length = 12, widget = forms.TextInput(attrs = {'class': 'form-control'}))

	class Meta:
		model = UserAccount
		fields = ('gender', 'marital_status', 'phone')


	
class RegistrationForm(forms.ModelForm):
	username =  forms.CharField(max_length = 128, help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'User Name', 'required': 'required'}))
	first_name = forms.CharField(max_length = 128, help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'First Name', 'required': 'required'}))
	last_name =  forms.CharField(max_length = 128, help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Last Name', 'required': 'required'}))
	email =  forms.EmailField(help_text = '', widget = forms.EmailInput(attrs = {'class':'form-control', 'Placeholder': 'Email', 'required': 'required'}))
	password =  forms.CharField(max_length = 15, help_text = '', widget = forms.PasswordInput(attrs = {'class':'form-control', 'Placeholder': 'Password', 'required': 'required'}))

	
	class Meta:
	
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password')

class LoginForm(forms.ModelForm):
	email = forms.EmailField(help_text = '', widget = forms.EmailInput(attrs = {'class':'form-control', 'Placeholder': 'Email', 'required': 'required'}))
	password = forms.CharField(max_length = 15, help_text = '', widget = forms.PasswordInput(attrs = {'class':'form-control', 'Placeholder': 'Password', 'required': 'required'}))

	class Meta:
		model = User
		fields = ('email', 'password')

class CheckoutForm(forms.ModelForm):
	first_name = forms.CharField(max_length = 128, help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'First Name', 'required': 'required'}))
	last_name =  forms.CharField(max_length = 128, help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Last Name', 'required': 'required'}))
	email =  forms.EmailField(help_text = '', widget = forms.EmailInput(attrs = {'class':'form-control', 'Placeholder': 'Email', 'required': 'required'}))
	# email = forms.EmailField(help_text = '', widget = forms.EmailInput(attrs = {'class':'form-control', 'Placeholder': 'Email', 'required': 'required'}))
	phone_number = forms.CharField(help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Phone Number', 'required': 'required'}))
	company_name = forms.CharField(help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Company Name',}))
	address1 = forms.CharField(help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Address 1', 'required': 'required'}))
	address2 = forms.CharField(help_text = '', widget = forms.TextInput(attrs = {'class':'form-control', 'Placeholder': 'Address 2',}))

