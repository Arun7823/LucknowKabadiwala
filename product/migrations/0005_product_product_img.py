# Generated by Django 4.0.4 on 2022-09-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='product/'),
        ),
    ]
