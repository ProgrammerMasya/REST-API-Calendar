from django.contrib import admin
from django.urls import path

from .views import UserCreateView, LoginView, LogoutView

urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]