from django.contrib import admin

# Register your models here.
from product.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "value", "discount", "stock")
