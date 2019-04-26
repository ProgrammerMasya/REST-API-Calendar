from django.urls import path, include
from .views import EventView, EventDayView, EventMonthView

urlpatterns = [
    path("events/", EventView.as_view()),
    path("events/day/", EventDayView.as_view()),
    path("events/month/", EventMonthView.as_view())
]