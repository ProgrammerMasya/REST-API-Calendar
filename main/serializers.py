from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    end_datetime = serializers.DateTimeField(required=False)

    class Meta:
        model = Event
        fields = (
            'user',
            'event_name',
            'start_datetime',
            'end_datetime',
        )

