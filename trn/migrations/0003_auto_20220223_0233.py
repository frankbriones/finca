# Generated by Django 2.2.4 on 2022-02-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trn', '0002_auto_20220223_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudpedido',
            name='fecha_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudpedido',
            name='fecha_recibida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
