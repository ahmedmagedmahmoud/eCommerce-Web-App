# Generated by Django 2.1 on 2018-10-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20181013_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address_final',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address_final',
            field=models.TextField(blank=True, null=True),
        ),
    ]