# Generated by Django 4.1.5 on 2023-06-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='author',
        ),
        migrations.AddField(
            model_name='auto',
            name='anno',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auto',
            name='precio',
            field=models.CharField(max_length=200),
        ),
    ]
