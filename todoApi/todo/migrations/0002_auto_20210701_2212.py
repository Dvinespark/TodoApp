# Generated by Django 3.2.5 on 2021-07-01 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 22, 12, 5, 57064)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
