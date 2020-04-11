from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .forms import register_form
from django.contrib import messages

def users(request):
  context  = {"msg": "This is the users page"}
  return render(request, 'users/index.html', context)

def login_page(request):
  context = {"msg": "This is the login page"}
  return render(request, 'users/login.html', context)

def register_page(request):
  if request.method == 'POST':
    form = register_form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Successfully registered your account!!!')
      return HttpResponseRedirect('login')
  context = {"form": register_form()}
  return render(request, 'users/register.html', context)