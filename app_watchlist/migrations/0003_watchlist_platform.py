# Generated by Django 3.2.14 on 2022-10-27 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_watchlist', '0002_auto_20220829_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='app_watchlist.streamplatform'),
            preserve_default=False,
        ),
    ]