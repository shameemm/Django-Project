# Generated by Django 4.1.1 on 2022-10-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0018_offers_max_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='offer_type',
            field=models.CharField(blank=True, default='product', max_length=200, null=True),
        ),
    ]
