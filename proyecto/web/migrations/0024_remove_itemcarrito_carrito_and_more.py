# Generated by Django 4.1.5 on 2023-07-11 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_carrito_itemcarrito_carrito_productos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrito',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
    ]