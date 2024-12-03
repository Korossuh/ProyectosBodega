# Generated by Django 4.2.16 on 2024-12-02 21:00

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(verbose_name='Numero de Telefono')),
                ('created', models.DateField(verbose_name='Fecha de Creacion: ')),
                ('update', models.DateField(verbose_name='Ultima Modificacion: ')),
                ('estado', models.IntegerField(verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mombre', models.CharField(max_length=50)),
                ('Modelo', models.CharField(max_length=50)),
                ('Stock', models.IntegerField(verbose_name='Stock')),
                ('estado', models.IntegerField(verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateField(verbose_name='Fecha de Creacion: ')),
                ('update', models.DateField(verbose_name='Ultima Modificacion: ')),
                ('estado', models.IntegerField(verbose_name='estado')),
                ('groups', models.ManyToManyField(blank=True, related_name='usuarios_groups', to='auth.group')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usuarios_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(max_length=1000)),
                ('estado', models.IntegerField()),
                ('id_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.docente', verbose_name='Id del Profesor')),
                ('id_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.materiales', verbose_name='ID del Material')),
            ],
        ),
    ]