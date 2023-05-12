from .models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name',' description', 'price', 'image', 'quantity',
        'discount', 'is_active', 'uploaded', 'created_at', 'category']


