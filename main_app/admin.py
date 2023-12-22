from django.contrib import admin

# Register your models here.
from .models import Car, Fueling

admin.site.register(Car)
admin.site.register(Fueling)