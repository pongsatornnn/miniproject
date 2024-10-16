# Generated by Django 5.0.6 on 2024-09-15 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_song_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.CreateModel(
            name='PlaylistSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_songs', to='myweb.playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.song')),
            ],
        ),
    ]
