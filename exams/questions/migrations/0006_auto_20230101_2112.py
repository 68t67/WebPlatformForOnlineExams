# Generated by Django 3.2.16 on 2023-01-01 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_auto_20230101_1658'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='exam',
            index_together={('slug', 'category')},
        ),
        migrations.AlterIndexTogether(
            name='progress',
            index_together={('user', 'exam')},
        ),
    ]