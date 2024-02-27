"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from endpoints.views import SubSubCategoryViewSet
from . import views
router=DefaultRouter()
router.register('subsubcategory',SubSubCategoryViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path('login',views.login),
    re_path('signup',views.signup),
    re_path('test_token',views.test_token),
    re_path('api/docs/schema/',SpectacularAPIView.as_view(),name='apischema'),
    re_path('api/docs/ui/',SpectacularSwaggerView.as_view()),
]+router.urls
