# Generated by Django 3.2.16 on 2022-11-17 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatetranslation', '0005_auto_20221117_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templatetranslation',
            old_name='user_authenticated',
            new_name='is_user_authenticated',
        ),
    ]
