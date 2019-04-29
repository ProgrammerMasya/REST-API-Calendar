from holidays.models import UserProfile

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "email",
            "username",
            "password",
            "country"
        ]
    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            country=validated_data["country"]
        )
        return user

    @staticmethod
    def get_message():
        return "Thank you for registering"


class UserLoginSerializer(ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = [
            "username",
            "password",
        ]
    extra_kwargs = {"password": {"write_only": True}}


