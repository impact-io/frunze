# Generated by Django 4.2.1 on 2023-05-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartabank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('activ', models.DateTimeField(max_length=16)),
                ('number', models.CharField(max_length=20)),
                ('INN', models.IntegerField(max_length=3)),
            ],
        ),
    ]
