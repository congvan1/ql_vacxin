from django.contrib import admin
from .models import Client, Vacxin, VacxinHistory, Illnesses

# Register your models here.
admin.site.register(Client)
admin.site.register(Vacxin)
admin.site.register(VacxinHistory)
admin.site.register(Illnesses)

