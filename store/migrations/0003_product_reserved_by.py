# Generated by Django 4.0.5 on 2022-07-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reserved_by',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
