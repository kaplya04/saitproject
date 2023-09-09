from django.db import models
from django.urls import reverse

# Create your models here.
class klient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100, verbose_name='Имя')
    phone = models.IntegerField()

    class Meta:
 #       db_table = 'klient'
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class poz_zakaz(models.Model):
    id = models.IntegerField(primary_key=True)
    tovar = models.TextField(max_length=100)
    kol_vo = models.IntegerField()
    zakaz = models.TextField(max_length=100)

    class Meta:
#        db_table = 'poz_zakaz'
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиция заказа'

    def __str__(self):
        return self.name


class tovar(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    cover = models.ImageField(upload_to='images/', blank=True)


    class Meta:
#        db_table = 'tovar'
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class zakaz(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    data_postavki = models.DateField()
    klient = models.TextField(max_length=100)
    statys = models.TextField(max_length=100)
    name = models.TextField(max_length=100,default=None)

    class Meta:
 #       db_table = 'zakaz'
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


class Images(models.Model):
    model_img = models.ImageField(upload_to="img/")


class postgrey(models.Model):
    name = models.TextField()

#    class Meta:
#        db_table = 'test4'
