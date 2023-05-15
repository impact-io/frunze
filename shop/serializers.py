from .models import Product, Category, Use
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'id']



class UseDetaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Use
        fields = '__all__'
