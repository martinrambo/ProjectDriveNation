# Generated by Django 4.1.5 on 2023-06-30 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_usuario_remove_cliente_contrasena'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]