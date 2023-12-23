from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Wash
from .forms import FuelingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def car_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', {
    'cars': cars
  })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  id_list = car.car_wash.all().values_list('id')
  exlcuded_washes = Wash.objects.exclude(id__in=id_list)
  fueling_form = FuelingForm()
  return render(request, 'cars/detail.html', {
    'car': car, 
    'fueling_form': fueling_form,
    'washes': exlcuded_washes
  })

class CarCreate(CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  fields = ['color', 'year', 'body_type']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'

def add_fueling(request, car_id):
  form = FuelingForm(request.POST)
  print(form)
  if form.is_valid():
    new_fueling = form.save(commit=False)
    new_fueling.car_id = car_id
    new_fueling.save()
  return redirect('detail', car_id=car_id)

class WashList(ListView):
  model = Wash

class WashDetail(DetailView):
  model = Wash

class WashCreate(CreateView):
  model = Wash
  fields = '__all__'

class WashUpdate(UpdateView):
  model = Wash
  fields = ['name', 'wash_type']

class WashDelete(DeleteView):
  model = Wash
  success_url = '/washes'

def assoc_wash(request, car_id, wash_id):
  Car.objects.get(id=car_id).car_wash.add(wash_id)
  return redirect('detail', car_id=car_id)

def unassoc_wash(request, car_id, wash_id):
  Car.objects.get(id=car_id).car_wash.remove(wash_id)
  return redirect('detail', car_id=car_id)