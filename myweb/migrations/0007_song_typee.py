# Generated by Django 5.0.6 on 2024-10-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_song_linkapple_song_linkspotify'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='typee',
            field=models.CharField(default='', max_length=200),
        ),
    ]
