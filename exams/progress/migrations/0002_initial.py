# Generated by Django 3.2.16 on 2023-01-23 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0002_initial'),
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersprint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='progress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='progress.progress', verbose_name='Прогресс'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='exams.question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='progress',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='exams.exam', verbose_name='Тестирование'),
        ),
        migrations.AddField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progression', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]