from rest_framework import serializers
from . models import Register , Shop 


class Userserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model=Register
        fields='__all__'
       



class Shopserializer(serializers.ModelSerializer):
    user=Userserializer(many=True)

    class Meta:
        model = Shop
        fields ='__all__'