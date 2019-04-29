from django.urls import path, include
from .views import *

urlpatterns = [
    path('save/', SaveHolidaysView.as_view()),
    path('', HolidayView.as_view())
]