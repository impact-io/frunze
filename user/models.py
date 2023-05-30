from django.db import models
from shop.models import Product

class Register(models.Model):
    passworld=models.IntegerField(max_length=20)
    user=models.CharField(max_length=114, blank=True)
    email= models.EmailField(max_length=1004, blank=True)


class Shop(models.Model):
    det= models.ForeignKey(Register, on_delete=models.CASCADE)
    shop=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='вход' )
     
    

