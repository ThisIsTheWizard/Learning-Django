from django.urls import path
from . import views

urlpatterns = [
  path('', views.users, name='users'),
  path('login/', views.login_page, name='login'),
  path('register/', views.register_page, name='register'),
]