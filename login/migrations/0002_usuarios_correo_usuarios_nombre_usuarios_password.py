# Generated by Django 4.2.16 on 2024-12-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='correo',
            field=models.CharField(default='Nada', max_length=50),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(default='Nada', max_length=50),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='password',
            field=models.CharField(default='Nada', max_length=50),
        ),
    ]
