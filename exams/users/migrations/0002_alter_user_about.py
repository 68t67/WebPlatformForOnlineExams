# Generated by Django 3.2.16 on 2023-01-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Обо мне'),
        ),
    ]
