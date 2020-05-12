from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flight, Passenger
from django.urls import reverse

def index(request):
  context = {"flights": Flight.objects.all()}
  return render(request, 'testing_app/flights.html', context)

def flight(request, flight_id):
  try:
    flight = Flight.objects.get(id=flight_id)
  except Flight.DoesNotExist:
    raise Http404("Flight Does Not Exist")
  context = {"flight": flight, "passengers": flight.passengers.all(), "non_passengers": Passenger.objects.exclude(flights=flight).all()}
  return render(request, 'testing_app/flight.html', context)

def book(request, flight_id):
  try:
    passenger_id = int(request.POST['passenger'])
    passenger = Passenger.objects.get(id=passenger_id)
    flight = Flight.objects.get(id=flight_id)
  except KeyError:
    return render(request, 'layout/error.html', {"msg": "No Selection"})
  except Passenger.DoesNotExist:
    return render(request, 'layout/error.html', {"msg": "No Passenger"})
  passenger.flights.add(flight)
  return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def single(request, flight_origin):
  context = {"flight": Flight.objects.get(origin=flight_origin)}
  return render(request, 'single.html', context)