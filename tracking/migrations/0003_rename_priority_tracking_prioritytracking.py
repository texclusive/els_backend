# Generated by Django 3.2.7 on 2021-10-27 18:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracking', '0002_rename_tracking_priority_tracking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Priority_tracking',
            new_name='PriorityTracking',
        ),
    ]
