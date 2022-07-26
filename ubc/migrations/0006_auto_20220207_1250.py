# Generated by Django 2.2.4 on 2022-02-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubc', '0005_auto_20220204_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudades',
            options={'permissions': {('crear_ciudades', 'Crear Ciudad'), ('editar_ciudades', 'Editar Ciudad'), ('actualizar_ciudades', 'Actualizar Ciudad')}},
        ),
        migrations.AlterModelOptions(
            name='lotes',
            options={'permissions': {('editar_lotes', 'Editar Lotes'), ('actualizar_lotes', 'Actualizar Lotes'), ('crear_lotes', 'Crear Lotes')}},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'permissions': {('editar_pais', 'Editar Pais'), ('crear_pais', 'Crear Pais'), ('actualizar_pais', 'Actualizar Pais')}},
        ),
        migrations.AlterModelOptions(
            name='sectores',
            options={'permissions': {('editar_sectores', 'Editar Sectores'), ('crear_sectores', 'Crear Sectores'), ('actualizar_sectores', 'Actualizar Sectores')}},
        ),
    ]
