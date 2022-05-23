from django.urls import path
from . import views
urlpatterns = [
	path('', views.Home, name='Home'),
	path('home/', views.Home, name='Home'),
	
	path('createClient/', views.createClient, name='createClient'),
	path('createVacxin/', views.createVacxin, name='createVacxin'),
	path('createIllnesses/', views.createIllnesses, name='createIllnesses'),

	path('viewClient/', views.viewClient, name='viewClient'),
	path('viewVacxin/', views.viewVacxin, name='viewVacxin'),
	path('signup/', views.SignUp, name='SignUp'),
]