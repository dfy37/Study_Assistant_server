from django.urls import path
from AppUserInfo import login

urlpatterns = [
    path('login', login.login),
]