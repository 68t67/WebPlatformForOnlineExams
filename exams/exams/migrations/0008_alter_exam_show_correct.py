# Generated by Django 3.2.16 on 2023-01-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_exam_show_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='show_correct',
            field=models.BooleanField(default=True, help_text='Только если активен параметр с отображением пользователю результатов', verbose_name='Отображать пользователю верные варианты ответов'),
        ),
    ]
