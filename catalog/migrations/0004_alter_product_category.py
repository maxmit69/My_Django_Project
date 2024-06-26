# Generated by Django 5.0.3 on 2024-03-29 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='catalog.category', verbose_name='категория'),
        ),
    ]
