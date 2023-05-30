from django.shortcuts import render
from .serializer import Userserializer, Register
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from shop.serializers import ProductSerializer,Product


class UserViewsets(viewsets.ModelViewSet):
    queryset=Register.objects.all()
    permission_classes=[
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class=Userserializer  
    def post(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class ShopViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    permission_classes=[
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class=ProductSerializer









