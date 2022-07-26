# Generated by Django 2.2.4 on 2022-02-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20220124_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriapersonal',
            options={'permissions': {('crear_categoria_personal', 'Crear Categoria Personal'), ('editar_categoria_personal', 'Editar Categoria Personal'), ('actualizar_categoria_personal', 'Actualizar Categoria Personal')}},
        ),
        migrations.AlterModelOptions(
            name='personalfinca',
            options={'permissions': {('actualizar_personal', 'Actualizar Categoria Personal'), ('editar_personal', 'Editar Personal'), ('crear_personal', 'Crear Personal')}},
        ),
        migrations.AlterModelOptions(
            name='tipopersonal',
            options={'permissions': {('editar_tipo_personal', 'Editar Tipo Personal'), ('actualizar_tipo_personal', 'Actualizar Tipo Personal'), ('crear_tipo_personal', 'Crear Tipo Personal')}},
        ),
    ]
