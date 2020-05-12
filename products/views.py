from django.shortcuts import render
from .models import Product

def all(request):
    context = {"products": Product.objects.all()}
    template = 'products/index.html'
    return render(request, template, context)

def single(request, product_slug):
    context = {"product": Product.objects.get(slug=product_slug)}
    template = 'products/single.html'
    return render(request, template, context)

