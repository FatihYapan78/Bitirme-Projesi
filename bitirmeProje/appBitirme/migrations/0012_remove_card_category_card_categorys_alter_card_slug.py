# Generated by Django 4.1.5 on 2023-02-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBitirme', '0011_card_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='category',
        ),
        migrations.AddField(
            model_name='card',
            name='categorys',
            field=models.ManyToManyField(to='appBitirme.category'),
        ),
        migrations.AlterField(
            model_name='card',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]