# Generated by Django 4.1.1 on 2022-10-26 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0002_rename_description_libro_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto',
            name='titulo',
        ),
    ]