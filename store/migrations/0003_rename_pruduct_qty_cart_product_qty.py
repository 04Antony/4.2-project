# Generated by Django 4.1 on 2022-10-21 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='pruduct_qty',
            new_name='product_qty',
        ),
    ]
