# Generated by Django 3.2.16 on 2022-11-17 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatetranslation', '0002_auto_20221117_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='templatetranslation',
            options={'ordering': ['view'], 'verbose_name': 'Traducción de template', 'verbose_name_plural': 'Traducciónes de templates'},
        ),
        migrations.RemoveField(
            model_name='templatetranslation',
            name='name',
        ),
    ]