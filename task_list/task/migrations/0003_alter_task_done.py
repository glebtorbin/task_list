# Generated by Django 3.2.16 on 2022-11-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_done_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
