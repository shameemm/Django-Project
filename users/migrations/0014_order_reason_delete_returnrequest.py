# Generated by Django 4.1.1 on 2022-10-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_returnrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reason',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='returnRequest',
        ),
    ]
