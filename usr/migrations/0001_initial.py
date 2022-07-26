# Generated by Django 2.1 on 2022-01-19 06:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bases', '0001_initial'),
        ('ubc', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bases.Estados')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('pais', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ubc.Pais')),
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
            name='Roles',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_crea', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modifica', models.IntegerField(blank=True)),
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bases.Estados')),
                ('grupo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='usuarios',
            name='rol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usr.Roles'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
