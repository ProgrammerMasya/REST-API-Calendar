from django.urls import path

from .views import UserCreateView, LoginView, LogoutView

urlpatterns = [
    path('registration/', UserCreateView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]