# Generated by Django 4.2 on 2024-05-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_version_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(auto_created=True, verbose_name='номер версии'),
        ),
    ]