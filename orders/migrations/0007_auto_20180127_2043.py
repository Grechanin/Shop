# Generated by Django 2.0.1 on 2018-01-27 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180122_2202'),
        ('orders', '0006_auto_20180127_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productinbasket',
            name='session_key',
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]