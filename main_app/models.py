from django.db import models
from django.urls import reverse

GAS =(
  ('U', 'Unleaded'),
  ('P', 'Unleaded Plus'),
  ('R', 'Premium Unleaded')
)

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  year = models.IntegerField()
  color = models.CharField(max_length=100)
  body_type = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.make} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Fueling(models.Model):
  date = models.DateField('fueling Date')
  gallons = models.DecimalField(max_digits=4, decimal_places=2)
  gas_type = models.CharField(
    max_length=1,
    choices=GAS,
    default=GAS[0][0]
  )
  cost = models.DecimalField(max_digits=5, decimal_places=2)

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f'Filled up {self.gallons} of {self.get_gas_type_display()} for ${self.cost} on {self.date}'
  
  class Meta:
    ordering = ['-date']