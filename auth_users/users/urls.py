from django.urls import path
from .views import login_view, register_view, logout_view, user_profile, update_profile

urlpatterns = [
    path('login/', login_view, name="login_page"),
    path('register/', register_view, name="register_page"),
    path('logout/', logout_view, name="logout_page"),
    path('profile/', user_profile, name="user_profile_page"),
    path('update/', update_profile, name="update_profile"),
]
