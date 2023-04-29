from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500)
    price = models.FloatField(verbose_name="baasy")
    image = models.ImageField(upload_to='images/products/')
    quantity = models.IntegerField(verbose_name="kolichestvo")
    discount = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    ordered_items = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.FloatField(verbose_name="jalpy baasy")
    created_at = models.DateField(auto_now=True)
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.phone
