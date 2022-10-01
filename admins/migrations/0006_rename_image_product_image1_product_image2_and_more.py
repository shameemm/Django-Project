# Generated by Django 4.1.1 on 2022-09-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images'),
        ),
    ]