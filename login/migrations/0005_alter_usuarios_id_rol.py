# Generated by Django 4.2.16 on 2024-12-02 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_usuarios_created_alter_usuarios_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id_rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.rol'),
        ),
    ]
