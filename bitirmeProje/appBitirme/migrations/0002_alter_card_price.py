# Generated by Django 4.1.5 on 2023-02-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(verbose_name='Ürün Fiyatı'),
        ),
    ]
