from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=3)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=9)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-image-url')  # s3 object link to image
    document_url = models.CharField(max_length=500, default='/no-doc-url') # s3 object link to document

    def __str__(self):
        return self.name
