# Generated by Django 3.2.16 on 2023-01-01 13:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20230101_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='priority',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='priority',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Приоритет'),
        ),
    ]