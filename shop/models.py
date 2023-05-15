from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()



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


class Use (models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    addres = models.CharField(verbose_name='адрес дома', max_length=100)
    phone = models.CharField(verbose_name='номер телефон', max_length=50)
    emil = models.CharField(verbose_name='email', max_length=100)
    pasword = models.CharField(verbose_name='password', max_length=100)
    created = models.DateField(auto_now=True, verbose_name='date_time')
    cart = models.CharField(verbose_name='номер карта', max_length=50)
    delivery = (
        (1, 'Доставка'),
        (2, 'Я сам возьму'),
    )
    tpye_delivery = models.IntegerField(verbose_name='Type_delivery', choices=delivery)
    # user = models.ForeignKey(User, verbose_name='Пользаватель', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
