from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.car_index, name='index'),
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_fueling/', views.add_fueling, name='add_fueling'),
  path('washes/', views.WashList.as_view(), name='wash_index'),
  path('washes/<int:pk>/', views.WashDetail.as_view(), name='wash_detail'),
  path('washes/create/', views.WashCreate.as_view(), name='wash_create'),
  path('washes/<int:pk>/update/', views.WashUpdate.as_view(), name='wash_update'),
  path('washes/<int:pk>/delete/', views.WashDelete.as_view(), name='wash_delete'),
  path('cars/<int:car_id>/washes/assoc_wash/<int:wash_id>/', views.assoc_wash, name='assoc_wash'),
  path('cars/<int:car_id>/washes/unassoc_wash/<int:wash_id>/', views.unassoc_wash, name='unassoc_wash')
]