from rest_framework import viewsets
from .serializers import *
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import generics



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated
    

class MainViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(discount__gte=0)


class CategorylistView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.filter()
    


class UseCreateView(generics.CreateAPIView):
    serializer_class = UseDetaiSerializer
    queryset = Use.objects.all()



class UseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UseDetaiSerializer
    queryset = Use.objects.all()


    