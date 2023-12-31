# Generated by Django 4.1.1 on 2022-12-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaplya', '0003_kategoria_news_delete_kategoriya_delete_modwin'),
    ]

    operations = [
        migrations.CreateModel(
            name='modal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Имя')),
                ('email', models.TextField(verbose_name='Почта')),
                ('problem', models.TextField(verbose_name='Проблема')),
            ],
        ),
        migrations.AlterField(
            model_name='kategoria',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
