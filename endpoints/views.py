
"""
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SubCategory, SubSubCategory
from server.serializers import SubSubCategorySerializer

class SubSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializer  # Add this line

    def list(self, request):
        subcategory = request.query_params.get('category')
        queryset = self.queryset
        if subcategory:
            queryset = queryset.filter(sub_category_name=subcategory)
        serializer = SubSubCategorySerializer(queryset, many=True)
        return Response(serializer.data)
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import serializers
from . import models


class AddCategory(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            category_serializer = serializers.CategorySerializer(data=request.data)

            category_serializer.is_valid(raise_exception=True)

            category_serializer.save()

            return Response({"message": "Success in adding 'Category' object"}, status.HTTP_201_CREATED)

        except Exception as e:
            print("Failed to store 'Category' Information: ", e)
            return Response({"error": "Error in adding 'Category' object"}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            category_name = request.data.get('name')
            category_obj = get_object_or_404(models.Category, name=category_name)

            category_obj.delete()
            return Response({"message": "Successfully deleted 'Category' object"}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Failed to delete 'Category' information: ", e)
            return Response({"error": "Error in deleting 'Category' object"}, status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            category_obj = get_object_or_404(models.Category, name="")  # bug

            category_serializer = serializers.CategorySerializer(category_obj, data=request.data, partial=True)

            category_serializer.is_valid(raise_exception=True)

            category_serializer.save()

            return Response({"message": "Successfully updated 'Category' object"}, status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print("Failed to update 'Category' information: ", e)
