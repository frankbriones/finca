# Generated by Django 2.2.4 on 2022-02-27 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0007_productos_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prv.Proveedores'),
        ),
    ]
