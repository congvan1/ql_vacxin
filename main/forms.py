from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Vacxin, VacxinHistory, Illnesses

class CreateNewVacxin(forms.ModelForm):
	class Meta:
		model = Vacxin
		fields = ['name', 'inject_times', 'price', 'manufacturer', 'description']

class CreateNewClient(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['name', 'sex', 'DOB', 'phone_number', 'address']

class CreateNewVacxinHistory(forms.ModelForm):
	class Meta:
		model = VacxinHistory
		fields = ['inject_date', 'inject_next_time']

class CreateNewIllnesses(forms.ModelForm):
	class Meta:
		model = Illnesses
		fields = ['name', 'description', 'prevention']

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

