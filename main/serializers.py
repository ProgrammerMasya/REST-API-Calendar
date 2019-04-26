from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'user',
            'event_name',
            'start_datetime',
            'end_datetime',
        )

