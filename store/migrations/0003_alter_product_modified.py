# Generated by Django 4.1 on 2022-08-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_prduct_name_product_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
