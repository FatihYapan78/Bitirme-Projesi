# Generated by Django 4.1.5 on 2023-03-25 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0021_favori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favori',
            name='image',
        ),
        migrations.RemoveField(
            model_name='favori',
            name='price',
        ),
        migrations.RemoveField(
            model_name='favori',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='favori',
            name='title',
        ),
        migrations.AddField(
            model_name='favori',
            name='urun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appBitirme.card', verbose_name='Ürün'),
        ),
    ]
