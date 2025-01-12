# Generated by Django 3.0.1 on 2021-01-27 23:49

import datetime

from django.db import migrations, models
from django.utils import timezone



class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0004_auto_20210128_0030"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="expense",
            options={"ordering": ["-date"]},
        ),
        migrations.AlterField(
            model_name="expense",
            name="date",
            field=models.DateTimeField(
                default=timezone.now

    ),
),

    ]
