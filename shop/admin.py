from django.contrib import admin
from .models import Product, Use



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'description']



@admin.register(Use)
class UseAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'emil', 'addres', 'created',
    'pasword', 'delivery', 'cart', 'tpye_delivery']