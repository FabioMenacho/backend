# Generated by Django 3.2.6 on 2021-08-26 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mesa_id', models.AutoField(primary_key=True, serialize=False)),
                ('mesa_nro', models.CharField(max_length=10)),
                ('mesa_cap', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('plato_id', models.AutoField(primary_key=True, serialize=False)),
                ('plato_nom', models.CharField(max_length=200)),
                ('plato_img', models.ImageField(blank=True, null=True, upload_to='platos')),
                ('plato_pre', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('categoria_id', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Platos', to='api.categoria')),
            ],
        ),
    ]