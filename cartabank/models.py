from django.db import models

# Create your models here.


class cartabank(models.Model):
    name=models.CharField(max_length=1000)
    activ=models.DateTimeField(max_length=16)
    number=models.CharField(max_length=20 )
    INN=models.IntegerField(max_length=3)
    

    def __str__(self):
        return self.name
