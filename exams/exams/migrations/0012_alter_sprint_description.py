# Generated by Django 3.2.16 on 2023-01-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0011_rename_about_sprint_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='Краткое описание'),
        ),
    ]