# Generated by Django 3.2.16 on 2022-12-18 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20221217_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uservariant',
            options={'ordering': ['-correct', '-selected'], 'verbose_name': 'Вариант ответа пользователя', 'verbose_name_plural': 'Варианты ответов пользователей'},
        ),
    ]