# Generated by Django 4.0.4 on 2022-06-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_bill_client_product_bill_product_bill_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='nit',
            field=models.IntegerField(max_length=300),
        ),
        migrations.AlterField(
            model_name='client',
            name='document',
            field=models.IntegerField(max_length=300),
        ),
    ]
