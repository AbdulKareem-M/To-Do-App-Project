# Generated by Django 5.1.5 on 2025-02-16 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_taskmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='user',
        ),
    ]
