# Generated by Django 2.0.1 on 2018-02-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20180204_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]