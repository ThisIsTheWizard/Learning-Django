from django.urls import path
from . import views

urlpatterns = [
  path('', views.all, name="products"),
  path('<slug:product_slug>/', views.single, name="product"),
]