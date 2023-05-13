from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import  ProductSerializer,CategorySerializer
from .models import Product
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated
    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Product.objects.all()
    
    def list(self, request, *args, **kwargs):
        cat = self.kwargs['cat_id']
        queryset = Product.objects.filter(category = cat)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class MainViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(discount__gte=0)
