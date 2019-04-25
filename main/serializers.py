from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Event
        fields = (
            'user',
            'event_name',
            'start_datetime',
            'end_datetime',
        )
