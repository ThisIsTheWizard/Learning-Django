from django.db import models

class Airport(models.Model):
  code = models.CharField(max_length=3)
  city = models.CharField(max_length=55)
  created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
    return f"{self.code}-{self.city}"

class Flight(models.Model):
  origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
  destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
  duration = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
    return f"{self.id}-{self.origin} to {self.destination}"

class Passenger(models.Model):
  firstname = models.CharField(max_length=99)
  lastname = models.CharField(max_length=99)
  flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
