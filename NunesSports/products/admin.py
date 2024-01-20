from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    ...


admin.site.register(Product, ProductAdmin)