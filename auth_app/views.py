from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(index):
  return HttpResponse("<h1>Home Page</h1>")