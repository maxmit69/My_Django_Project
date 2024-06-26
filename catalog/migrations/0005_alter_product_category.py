# Generated by Django 5.0.3 on 2024-03-30 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0004_alter_product_category'),
    ]

    operations = (
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='catalog.category', verbose_name='категория'),
        ),
    )
