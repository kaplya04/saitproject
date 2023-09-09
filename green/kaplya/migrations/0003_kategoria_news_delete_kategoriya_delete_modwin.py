# Generated by Django 4.1.1 on 2022-12-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaplya', '0002_modwin_remove_kategoriya_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('cover', models.TextField()),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaplya.kategoria')),
            ],
        ),
        migrations.DeleteModel(
            name='kategoriya',
        ),
        migrations.DeleteModel(
            name='modwin',
        ),
    ]
