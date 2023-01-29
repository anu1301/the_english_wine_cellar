from django.contrib import admin
from .models import Product, Category

# Models registered here
admin.site.register(Product)
admin.site.register(Category)
