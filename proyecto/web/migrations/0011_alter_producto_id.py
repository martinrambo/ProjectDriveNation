# Generated by Django 4.1.5 on 2023-06-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
