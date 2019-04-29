from django.urls import path, include
from .views import *

urlpatterns = [
    path('save/', SaveHolidaysView.as_view(), name="save_holidays"),
    path('', HolidayView.as_view(), name="holidays")
]