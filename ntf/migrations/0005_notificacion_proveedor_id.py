# Generated by Django 2.2.4 on 2022-07-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntf', '0004_notificacion_orden_prv'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='proveedor_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
