# Generated by Django 3.2.6 on 2021-08-27 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20210825_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='mesa_id',
            field=models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Pedido', to='api.mesa', verbose_name='Mesa'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usu_id',
            field=models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Pedido', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='pedidoplatos',
            name='pedido_id',
            field=models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.pedido', verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='pedidoplatos',
            name='plato_id',
            field=models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.plato', verbose_name='Plato'),
        ),
    ]