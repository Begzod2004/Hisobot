# Generated by Django 4.1 on 2022-08-30 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_category_hisobot_daromad_hisobot_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="xarajatlar",
            name="hisobot",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.hisobot",
            ),
            preserve_default=False,
        ),
    ]
