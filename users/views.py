from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

def index(request):
  if not request.user.is_authenticated:
    return render(request, 'user/login.html', {"msg": "Login To See The Home Page"})
  context = {"user": request.user}
  return render(request, 'user/index.html', context)

def login_view(request):
  user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
  if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse("user"))
  else:
    return render(request, 'user/login.html', {"msg": "Wrong Credentials"})

def logout_view(request):
  logout(request)
  return render(request, 'user/login.html', {"msg": "Logged Out"})

def registration(request):
  user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
  user.save()
  return render(request, 'user/login.html', {"msg": "Successfully Registered!!! You can Login Here Now"})

def registration_view(request):
  return render(request, 'user/registration.html', {"msg": "Don't Have Any Account, Register Here"})


