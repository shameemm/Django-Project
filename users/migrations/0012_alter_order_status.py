# Generated by Django 4.1.1 on 2022-10-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_order_cancel_alter_order_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Order Confirmed', max_length=100),
        ),
    ]
