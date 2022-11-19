# Generated by Django 3.2.16 on 2022-11-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatetranslation', '0004_auto_20221117_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatetranslation',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre de template'),
        ),
        migrations.AddField(
            model_name='templatetranslation',
            name='user_authenticated',
            field=models.BooleanField(default=False, verbose_name='¿Usuario autenticado?'),
        ),
        migrations.AlterField(
            model_name='templatetranslation',
            name='view',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre de vista'),
        ),
    ]
