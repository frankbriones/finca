# Generated by Django 2.2.4 on 2022-02-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='cantidad_existente',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='cantidad_minima',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
