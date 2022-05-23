from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewVacxin, CreateNewClient, CreateNewVacxinHistory, CreateNewIllnesses, SignUpForm
from .models import Client, Vacxin, VacxinHistory, Illnesses
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def Home(request):
	return render(request, 'main/home.html',{})

@login_required(login_url="/login")
def createClient(request):
	if request.method == 'POST':
		form = CreateNewClient(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			client.save()
			return redirect('/viewClient')
	else:
		form = CreateNewClient()
	return render(request, 'main/createClient.html', {'form':form})

@login_required(login_url="/login")
def createVacxin(request):
	if request.method == 'POST':
		form = CreateNewVacxin(request.POST)
		if form.is_valid():
			vacxin = form.save(commit=False)
			vacxin.save()
			return redirect('/home')
	else:
		form = CreateNewVacxin()
	return render(request, 'main/createVacxin.html', {'form':form})

@login_required(login_url="/login")
def createIllnesses(request):
	if request.method == 'POST':
		form = CreateNewIllnesses(request.POST)
		if form.is_valid():
			illnesses = form.save(commit=False)
			illnesses.save()
			return redirect('/createIllnesses')
	else:
		form = CreateNewIllnesses()
	return render(request, 'main/createIllnesses.html', {'form':form})


def viewClient(request):
	clients = Client.objects.all()
	vacxins = Vacxin.objects.all()
	if request.method == "POST":
		if request.POST.get("C_delete"):
			clientID = request.POST.get("C_delete")
			client = Client.objects.get(id=clientID)
			client.delete()

		elif request.POST.get("C_save"):
			for client in clients:
				if request.POST.get('r' + str(client.id)) == "Male":
					client.sex = True
				else: 
					client.sex = False
				client.name = request.POST.get('n' + str(client.id))
				client.address = request.POST.get('adr' + str(client.id))
				client.phone_number = request.POST.get('pn' + str(client.id))
				client.save()

		elif request.POST.get("C_view"):
			clientID = request.POST.get("C_view")
			client = Client.objects.get(id=clientID)
			History = client.vacxinhistory_set.all()
			totalPrice = 0
			for his in History:
				totalPrice += int(his.vacxin.price)
			return render(request, 'main/viewInjectHistory.html', {'vacxinHistory': History, 'vacxins':vacxins, 'client':client, 'totalPrice':totalPrice})

		elif request.POST.get("Injected_add"):
			clientID = request.POST.get("Injected_add")
			client = Client.objects.get(id=clientID)
			
			if request.POST.get('VacxinSelected'):
				vacxinID = request.POST.get('VacxinSelected')
				vacxin = Vacxin.objects.get(id=vacxinID)
				vacxinHistory = VacxinHistory.objects.create(client=client, vacxin=vacxin)
				vacxinHistory.save()
				History = client.vacxinhistory_set.all()
				totalPrice = 0
				for his in History:
					totalPrice += int(his.vacxin.price)
			return render(request, 'main/viewInjectHistory.html', {'vacxinHistory': History,'vacxins':vacxins, 'client':client, 'totalPrice':totalPrice})
		
		elif request.POST.get("his_delete"):
			hisID = request.POST.get('his_delete')
			his = VacxinHistory.objects.get(id=hisID)
			clientID = his.client.id
			client = Client.objects.get(id=clientID) 
			History = client.vacxinhistory_set.all()
			his.delete()
			totalPrice = 0
			for his in History:
				totalPrice += int(his.vacxin.price)
			return render(request, 'main/viewInjectHistory.html', {'vacxinHistory': History,'vacxins':vacxins, 'client':client, 'totalPrice':totalPrice})


	return render(request, 'main/viewClient.html', {'clients':clients})


def viewVacxin(request):
	vacxins = Vacxin.objects.all()
	illnesses = Illnesses.objects.all()
	if request.method == "POST":
		if request.POST.get("Ill_delete"):
			illID,vacxinID = request.POST.get("Ill_delete").split(",")
			ill = Illnesses.objects.get(id=illID)
			vacxin = Vacxin.objects.get(id=vacxinID)
			vacxin_ill = vacxin.illnesses.all()
			vacxin.illnesses.remove(ill)

			return render(request, 'main/viewIllnesses.html', {'vacxin':vacxin, 'illnesses':illnesses, 'vacxin_ill':vacxin_ill})
		elif request.POST.get("Ill_save"):
			vacxinID = request.POST.get('Ill_save')
			vacxin = Vacxin.objects.get(id=vacxinID)
	
			vacxin_ill = vacxin.illnesses.all()
			for ill in vacxin_ill:
				ill.name = request.POST.get('name' + str(ill.id))
				ill.description = request.POST.get('desc' + str(ill.id))
				ill.prevention = request.POST.get('preve' + str(ill.id))
				ill.save()
			illnesses = Illnesses.objects.all()
			return render(request, 'main/viewIllnesses.html', {'vacxin':vacxin, 'illnesses':illnesses, 'vacxin_ill':vacxin_ill})

		elif request.POST.get("ill_view"):
			vacxinID = request.POST.get('ill_view')
			vacxin = Vacxin.objects.get(id=vacxinID)
			vacxin_ill = vacxin.illnesses.all()
			return render(request, 'main/viewIllnesses.html', {'vacxin':vacxin, 'illnesses':illnesses, 'vacxin_ill':vacxin_ill})

		elif request.POST.get("newIllnesses"):
			vacxinID = request.POST.get('newIllnesses')
			vacxin = Vacxin.objects.get(id=vacxinID)
			if request.POST.get('VacxinSelected'):
				illID = request.POST.get('VacxinSelected')
				ill = Illnesses.objects.get(id=illID)
				vacxin.illnesses.add(ill)
				vacxin_ill = vacxin.illnesses.all()
			return render(request, 'main/viewIllnesses.html', {'vacxin':vacxin, 'illnesses':illnesses, 'vacxin_ill':vacxin_ill})
		elif request.POST.get("vacxin_save"):
			for vacxin in vacxins:
				vacxin.name = request.POST.get("name" + str(vacxin.id))
				vacxin.inject_times = request.POST.get("inject_times" + str(vacxin.id))
				vacxin.price = request.POST.get("price" + str(vacxin.id))
				vacxin.manufacturer = request.POST.get("manufacturer" + str(vacxin.id))
				vacxin.description = request.POST.get("description" + str(vacxin.id))
				vacxin.save()

		elif request.POST.get("vacxin_delete"):
			vacxID = request.POST.get("vacxin_delete")
			vacxin = Vacxin.objects.get(id=vacxID)
			vacxin.delete()

	return render(request, 'main/viewVacxin.html', {'vacxins':vacxins})

def SignUp(response):
	if response.method == "POST":
		form = SignUpForm(response.POST)
		if form.is_valid():
			user = form.save()
			login(response, user)
			return redirect("/login")
	else:
		form = SignUpForm()

	return render(response, 'registration/sign_up.html', {'form':form})
