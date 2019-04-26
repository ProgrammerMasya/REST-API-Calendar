from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]
    extra_kwargs = {"password": {"write_only": True}}

    @staticmethod
    def get_message():
        return "Thank you for registering"


class UserLoginSerializer(ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
    extra_kwargs = {"password": {"write_only": True}}
