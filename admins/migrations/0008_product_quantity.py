# Generated by Django 4.1.1 on 2022-10-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0007_rename_image1_product_image_remove_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
