# Generated by Django 3.2.14 on 2022-11-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_watchlist', '0005_review_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='update',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
