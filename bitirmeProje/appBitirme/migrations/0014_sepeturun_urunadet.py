# Generated by Django 4.1.5 on 2023-03-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0013_sepeturun'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepeturun',
            name='urunadet',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Ürün Adet'),
        ),
    ]
