# Generated by Django 2.0.13 on 2020-12-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmezapp', '0012_auto_20201203_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]