from django.db import models



class User(models.Model):
    delivery = (
        (1, 'Доставка'),
        (2, 'Я сам возьму'),
    )
    floor = (
        (1, 'Женщина'),
        (2, 'Мужчина'),
    )
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    addres = models.CharField(verbose_name='адрес дома', max_length=100)
    phone = models.CharField(verbose_name='номер телефон', max_length=50)
    emil = models.CharField(verbose_name='email', max_length=100)
    pasword = models.CharField(verbose_name='password', max_length=100)
    created = models.DateField(auto_now=True, verbose_name='date_time')
    cart = models.CharField(verbose_name='номер карта', max_length=50)
    floor_pol = models.IntegerField(verbose_name='Пол',choices=floor)
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    tpye_delivery = models.IntegerField(verbose_name='Type_delivery', choices=delivery)

    def __str__(self):
        return self.name


