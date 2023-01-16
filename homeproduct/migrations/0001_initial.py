# Generated by Django 4.0.4 on 2022-09-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('product_img', models.FileField(default=None, max_length=250, null=True, upload_to='product/')),
            ],
        ),
    ]