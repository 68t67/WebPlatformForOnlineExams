# Generated by Django 3.2.16 on 2023-01-14 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0006_auto_20230114_2257'),
        ('progress', '0003_alter_progress_guest_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='started',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала'),
        ),
        migrations.CreateModel(
            name='UserSprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('finished', models.DateTimeField(null=True, verbose_name='Дата завершения')),
                ('completed', models.BooleanField(null=True, verbose_name='Завершен')),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='exams.sprint', verbose_name='Спринт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пройденный спринт',
                'verbose_name_plural': 'Пройденные спринты',
            },
        ),
    ]
