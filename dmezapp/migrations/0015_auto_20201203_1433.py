# Generated by Django 2.0.13 on 2020-12-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmezapp', '0014_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mrp_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
