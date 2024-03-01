
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from endpoints.models import SubSubCategory
from endpoints.models import SubCategory
# serialization is the process of converting complex datatypes into naive python types
# deserialization is the process of converting JSON or XML into complextypes
# complex data types here refers to custom data models and django models
class UserSerializer(serializers.ModelSerializer): # this deserializes the JSON payload into
    # a user model that is provided by django
    class Meta(object):
        model=User
        fields=['id','username','password','email']
class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubSubCategory
        fields="__all__"
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields="__all__"
"""