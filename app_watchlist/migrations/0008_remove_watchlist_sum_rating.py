# Generated by Django 3.2.14 on 2022-11-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_watchlist', '0007_watchlist_sum_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='sum_rating',
        ),
    ]
