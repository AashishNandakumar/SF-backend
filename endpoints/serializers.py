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


class SubCategorySerializerOnId(serializers.ModelSerializer):

    category_id = serializers.SerializerMethodField('get_category_id2')
    print(category_id)

    def get_category_id2(self, obj):
        print("categoryId: ", self.context.get('categoryId'))
        return self.context.get('categoryId')

    class Meta:
        model = models.SubCategory
        fields = ["name", "description", "image_url", "category_id"]


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubCategory
        fields = "__all__"


class SubSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubSubCategory
        fields = "__all__"


class SubSubCategorySerializerOnId(serializers.ModelSerializer):

    sub_category_id = serializers.SerializerMethodField('get_sub_sub_category_id')

    def get_sub_sub_category_id(self, obj):
        return self.context.get('subCategoryId')

    class Meta:
        model = models.SubSubCategory
        fields = ["name", "description", "image_url", "sub_category_id"]
