# Generated by Django 4.1.1 on 2022-10-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_order_reason_delete_returnrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price_with_offer',
            field=models.FloatField(default=0),
        ),
    ]
