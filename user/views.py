from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializers import UserDetailSerializer
from .models import User
from rest_framework import viewsets



class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
