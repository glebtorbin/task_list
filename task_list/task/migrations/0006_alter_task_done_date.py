# Generated by Django 3.2.16 on 2022-11-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_done_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_date',
            field=models.DateField(verbose_name='Дата выполнения'),
        ),
    ]
