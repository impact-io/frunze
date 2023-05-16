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
<<<<<<< HEAD



class UseDetaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Use
        fields = '__all__'
=======
>>>>>>> 0a71395798dd9ed9efce4dff3be27435805c380b
