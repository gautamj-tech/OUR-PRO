# Generated by Django 2.0.13 on 2020-12-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmezapp', '0011_auto_20201202_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
