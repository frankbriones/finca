# Generated by Django 2.2.4 on 2022-02-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubc', '0006_auto_20220207_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='prefijo_cel',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
