# Generated by Django 2.2.4 on 2022-07-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntf', '0003_auto_20220308_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='orden_prv',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
