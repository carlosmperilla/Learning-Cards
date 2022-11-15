# Generated by Django 3.2.16 on 2022-11-15 04:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['foreign_word'], 'verbose_name': 'Card', 'verbose_name_plural': 'Cards'},
        ),
        migrations.AlterField(
            model_name='card',
            name='hits',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999)], verbose_name='Aciertos'),
        ),
        migrations.AlterField(
            model_name='card',
            name='mistakes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999)], verbose_name='Errores'),
        ),
    ]