from django.db import models


# Create your models here.
class Kategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Modal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(verbose_name="Имя")
    email = models.TextField(verbose_name="Почта")
    problem = models.TextField(verbose_name="Проблема")
    number = models.TextField(verbose_name="Номер")

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'

    def __str__(self):
        return self.problem


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/', blank=True)
    kategoria = models.ForeignKey(Kategoria, models.CASCADE)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name


