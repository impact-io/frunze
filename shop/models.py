from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name="baasy")
    image = models.ImageField(upload_to='images/products/')
    quantity = models.IntegerField(verbose_name="kolichestvo", )
    discount = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
