from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from .models import SubCategory
from .models import SubSubCategory
from server.serializers import SubSubCategorySerializer

class SubSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubSubCategory.objects.all()
    def list(self,request):
        subcategory=request.query_params.get('category')
        queryset=self.queryset
        if subcategory:
            queryset=queryset.filter(sub_category_name=subcategory)
        serializer=SubSubCategorySerializer(queryset, many=True)
        return Response(serializer.data)