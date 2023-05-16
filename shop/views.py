from rest_framework import viewsets
from .serializers import  ProductSerializer, CategoryListSerializer
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated
    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListSerializer
    queryset = Product.objects.all()
    
    def list(self, request, *args, **kwargs):
        cat = self.kwargs['cat_id']
        queryset = Product.objects.filter(category = cat)
        serializer = CategoryListSerializer(queryset, many=True)
        return Response(serializer.data)


class MainViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(discount__gte=0)


class CategorylistView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.filter()
    
