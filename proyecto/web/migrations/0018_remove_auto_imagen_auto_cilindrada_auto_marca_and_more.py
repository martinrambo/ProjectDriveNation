# Generated by Django 4.1.5 on 2023-07-08 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_imagenauto_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='auto',
            name='cilindrada',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='auto',
            name='marca',
            field=models.CharField(default='generico', max_length=200),
        ),
        migrations.AddField(
            model_name='auto',
            name='modelo',
            field=models.CharField(default='generico', max_length=200),
        ),
    ]
