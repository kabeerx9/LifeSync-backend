# Generated by Django 5.0.6 on 2024-06-22 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_delete_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='position',
        ),
    ]