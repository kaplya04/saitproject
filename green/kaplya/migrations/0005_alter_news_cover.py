# Generated by Django 4.1.4 on 2022-12-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaplya', '0004_modal_alter_kategoria_id_alter_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]