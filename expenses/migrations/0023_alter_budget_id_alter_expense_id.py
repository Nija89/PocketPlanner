# Generated by Django 5.1.4 on 2024-12-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0022_auto_20230830_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
