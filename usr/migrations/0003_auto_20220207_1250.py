# Generated by Django 2.2.4 on 2022-02-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0002_auto_20220206_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='GruposPermisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'permissions': {('editar_rol', 'Editar Rol'), ('crear_rol', 'Crear Rol'), ('actualizar_rol', 'Actualizar Rol')}},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'permissions': {('actualizar_usuarios', 'Actualizar Usuarios'), ('editar_usuarios', 'Editar Usuarios'), ('crear_usuarios', 'Crear Usuarios')}},
        ),
    ]
