# Generated by Django 3.2.16 on 2022-11-14 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_done_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнения'),
        ),
    ]