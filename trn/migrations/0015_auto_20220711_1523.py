# Generated by Django 2.2.4 on 2022-07-11 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trn', '0014_auto_20220711_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordenbodega',
            options={'permissions': {('actualizar_orden_ingreso', 'Actualizar Orden de Ingreso'), ('ver_orden_salida', 'Ver Ordenes de Salida de Bodega'), ('ver_orden_ingreso', 'Ver Orden de Ingreso a Bodega'), ('crear_orden_ingreso', 'Agregar Orden de Ingreso')}},
        ),
    ]
