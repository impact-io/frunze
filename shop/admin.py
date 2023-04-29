from django.contrib import admin
from .models import Product, Order, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'description']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['ordered_items', 'phone']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']