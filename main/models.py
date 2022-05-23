from django.db import models
from datetime import date
from django.contrib.auth.models import User
from dateutil import relativedelta

# Create your models here.
class Client(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client', null=True)
	name = models.CharField(max_length=200)
	phone_number = models.PositiveIntegerField(default=0)
	address = models.CharField(max_length=200)
	DOB = models.DateField(default=date.today)
	sex = models.BooleanField(default=False)

	def __str__(self):
		s = str(self.name) + "," + str(self.phone_number) + "," + str(self.sex) + "," + str(self.DOB) + "," + str(self.address)
		return s 

class Illnesses(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=5000)
	prevention = models.CharField(max_length=5000)
	def __str__(self):
		s = str(self.name) + "," + str(self.description)
		return s 

class Vacxin(models.Model):
	illnesses = models.ManyToManyField(Illnesses)
	name = models.CharField(max_length=200)
	inject_times = models.PositiveSmallIntegerField(default=1)
	description = models.CharField(max_length=5000)
	price = models.PositiveIntegerField(default=0)
	manufacturer = models.CharField(max_length=200)

	def __str__(self):
		s = str(self.name) + "," + str(self.inject_times) + "," + str(self.description) + "," + str(self.price) + "," + str(self.manufacturer)
		return self.name

class VacxinHistory(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	vacxin = models.ForeignKey(Vacxin, on_delete=models.CASCADE)
	inject_date = models.DateField(default=date.today)
	next_month = date.today() + relativedelta.relativedelta(months=1)
	inject_next_time = models.DateField(default=next_month)


	def __str__(self):
		s = str(self.inject_date) + "," + str(self.inject_next_time) 
		return s 





