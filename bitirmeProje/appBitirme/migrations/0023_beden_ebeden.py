# Generated by Django 4.1.5 on 2023-03-27 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appBitirme', '0022_remove_favori_image_remove_favori_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Beden')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Beden')),
            ],
        ),
        migrations.CreateModel(
            name='EBeden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='Ürün Fiyatı')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok')),
                ('beden', models.CharField(max_length=50, verbose_name='Beden')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBitirme.card', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
