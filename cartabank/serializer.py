from .models import cartabank
from rest_framework import serializers


class Cartaserializer(serializers.ModelSerializer):

    class Meta:
        model=cartabank
        fields="__all__"