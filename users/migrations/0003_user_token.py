# Generated by Django 4.2 on 2024-05-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='токен'),
        ),
    ]
