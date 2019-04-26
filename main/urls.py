from django.urls import path, include
from .views import EventView, EventDayView

urlpatterns = [
    path("events/", EventView.as_view()),
    path("events/day/", EventDayView.as_view()),
]