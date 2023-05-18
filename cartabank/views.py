
from django.shortcuts import render
from .serializer import Cartaserializer
from rest_framework import permissions,serializers,viewsets
from . models import cartabank


# Create your views here.

class CartabankviewSet(viewsets.ModelViewSet):
    queryset=cartabank.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=Cartaserializer

