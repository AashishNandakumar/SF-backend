from django.urls import path
from . import views

# All you backend endpoints go here
urlpatterns = [
    path("add-category/", views.AddCategory.as_view()),
]
