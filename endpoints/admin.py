from django.contrib import admin
from . import models

# Register your models here.
"""
from .models import SubCategory
from .models import SubSubCategory
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
"""

admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.SubSubCategory)
