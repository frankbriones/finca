# Generated by Django 2.2.4 on 2022-02-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bases', '0002_configuracionsistema'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_crea', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modifica', models.IntegerField(blank=True)),
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bases.Estados')),
            ],
            options={
                'permissions': {('actualizar_categoria_prd', 'Actualizar Categoria Prducto'), ('editar_categoria_prd', 'Editar Categoria Prducto'), ('crear_categoria_prd', 'Crear Categoria Producto')},
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_crea', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modifica', models.IntegerField(blank=True)),
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bases.Estados')),
            ],
            options={
                'permissions': {('editar_unidad_meidida', 'Editar Unidad Medida'), ('actualizar_unidad_meidida', 'Actualizar Unidad Medida'), ('crear_unidad_meidida', 'Crear Unidad Medida')},
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_crea', models.IntegerField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modifica', models.IntegerField(blank=True)),
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='prd.CategoriaProducto')),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bases.Estados')),
                ('unidad_medida', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='prd.UnidadMedida')),
            ],
            options={
                'permissions': {('crear_producto', 'Crear Producto'), ('editar_producto', 'Editar Prducto'), ('actualizar_producto', 'Actualizar Prducto')},
            },
        ),
    ]
