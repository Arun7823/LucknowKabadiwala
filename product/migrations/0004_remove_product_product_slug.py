# Generated by Django 4.0.4 on 2022-09-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_slug_product_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_slug',
        ),
    ]
