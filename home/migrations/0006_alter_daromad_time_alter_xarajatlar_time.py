# Generated by Django 4.1 on 2022-08-30 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_xarajatlar_hisobot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="daromad",
            name="time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="xarajatlar",
            name="time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]