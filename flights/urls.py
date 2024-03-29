from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:flight_id>', views.flight, name='flight'),
  path('<int:flight_id>/booking', views.book, name='book'),
  path('single/<int:flight_origin>/', views.single, name='single'),
]