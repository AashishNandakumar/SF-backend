from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer): # this deserializes the JSON payload into
    # a user model that is provided by django
    class Meta(object):
        model=User
        fields=['id','username','password','email']