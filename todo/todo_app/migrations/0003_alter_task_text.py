# Generated by Django 4.1.2 on 2022-11-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_status_task_publishing_status_board_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.CharField(max_length=150),
        ),
    ]