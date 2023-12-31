# Generated by Django 4.1.1 on 2022-10-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='klient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('adres', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
            options={
                'db_table': 'klient',
            },
        ),
        migrations.CreateModel(
            name='poz_zakaz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tovar', models.CharField(max_length=100)),
                ('kol_vo', models.IntegerField()),
                ('zakaz', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'poz_zakaz',
            },
        ),
        migrations.CreateModel(
            name='tovar',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'tovar',
            },
        ),
        migrations.CreateModel(
            name='zakaz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('data_postavki', models.DateField()),
                ('time_postavki', models.DateTimeField()),
                ('klient', models.CharField(max_length=100)),
                ('statys', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'zakaz',
            },
        ),
    ]
