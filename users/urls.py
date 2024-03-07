"""URLs patterns for users app."""

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
]
