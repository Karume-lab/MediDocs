from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "password")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            "url",
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
        ]

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(**validated_data)
        return user
