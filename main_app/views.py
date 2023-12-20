from django.shortcuts import render

cars = [
  {'make': 'BMW', 'model': '328i', 'year': 1999, 'color': 'Blue', 'body_type': 'Sedan'},
  {'make': 'Chevy', 'model': 'Traverse', 'year': 2014, 'color': 'white', 'body_type': 'Suv'},
  {'make': 'Porsche', 'model': '911', 'year': 2020, 'color': 'Teal', 'body_type': 'Coupe'},
  {'make': 'Volkswagen', 'model': 'Jetta', 'year': 2009, 'color': 'Black', 'body_type': 'Wagon'},
  {'make': 'Honda', 'model': 'Civic', 'year': 1996, 'color': 'Red', 'body_type': 'Hatchback'},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def car_index(request):
  return render(request, 'cars/index.html', {
    'cars': cars
  })