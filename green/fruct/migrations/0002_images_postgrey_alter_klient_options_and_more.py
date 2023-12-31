# Generated by Django 4.1.1 on 2022-12-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_img', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='postgrey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='klient',
            options={'verbose_name': 'Клиенты', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='poz_zakaz',
            options={'verbose_name': 'Позиция заказа', 'verbose_name_plural': 'Позиция заказа'},
        ),
        migrations.AlterModelOptions(
            name='tovar',
            options={'verbose_name': 'Товары', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='zakaz',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='klient',
            name='adres',
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='time_postavki',
        ),
        migrations.AddField(
            model_name='tovar',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='zakaz',
            name='name',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='klient',
            name='name',
            field=models.TextField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='poz_zakaz',
            name='tovar',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='poz_zakaz',
            name='zakaz',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='klient',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='statys',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='klient',
            table=None,
        ),
        migrations.AlterModelTable(
            name='poz_zakaz',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tovar',
            table=None,
        ),
        migrations.AlterModelTable(
            name='zakaz',
            table=None,
        ),
    ]
