from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class CustomUserCreateSerializer(UserCreateSerializer):  # The default 'UserCreateSerializer' was not saving first_name and last_name, hence this part exists
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["username", "password", "first_name", "last_name"]  # save these fields into 'User' model


class CustomUserSerializer(UserSerializer):  # the default 'UserSerializer' was returning username, email, id. But I wanted username, first_name, last_name, so I made my own implementation
    class Meta(UserSerializer.Meta):
        model = User
        fields = ["username", "first_name", "last_name"]  # display only these fields


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
