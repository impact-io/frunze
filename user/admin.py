from django.contrib import admin
from .models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['delivery', 'surname', 'name', 'addres', 'phone', 'emil',
    'pasword', 'created', 'cart', 'tpye_delivery']


