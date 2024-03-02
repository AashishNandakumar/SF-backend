from django.urls import path
from . import views

# All you backend endpoints go here
urlpatterns = [
    path("categories", views.CategoryBulk.as_view()),  # GET, POST. Fetch and Add Categories
    path("categories/<int:categoryId>", views.CategoryParticular.as_view()),  # DELETE, PATCH. Delete and Update Categories
    path("category/<int:categoryId>/sub-category", views.SubCategoryBulk.as_view()),  # GET, POST. Fetch and Add SubCategories
    path("category/<int:categoryId>/sub-category/<int:subCategoryId>", views.SubCategoryParticular.as_view()),  # DELETE, PATCH. Delete and Update SubCategories
    path("category/<int:categoryId>/sub-category/<int:subCategoryId>/sub-sub-category", views.SubSubCategoryBulk.as_view()),  # GET, POST. Fetch and Add SubSubCategories
    path("category/<int:categoryId>/sub-category/<int:subCategoryId>/sub-sub-category/<int:subSubCategoryId>", views.SubSubCategoryParticular.as_view()),  # DELETE, PATCH. Delete and Update SubSubCategories
    path("generate-uuid", views.GenerateUUID.as_view()),  # GET. Fetch UUID to rename the files from the client(so that every filename in S3 is unique)
    path("generate-signed-url-and-store-reference", views.GenerateSignedURLAndStoreReference.as_view()),  # GET. Fetch signed URL, push the file to S3, give back the file details to backend so that it stores the reference to S3

]
