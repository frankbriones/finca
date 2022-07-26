# Generated by Django 2.2.4 on 2022-08-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_delete_personalfinca'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalFinca',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_crea', models.IntegerField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modifica', models.IntegerField(blank=True)),
                ('id_personal', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=350)),
                ('apellidos', models.CharField(max_length=350)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='categoriapersonal',
            name='usuario_crea',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tipopersonal',
            name='usuario_crea',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
