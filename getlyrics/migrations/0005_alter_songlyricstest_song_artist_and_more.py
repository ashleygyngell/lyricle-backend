# Generated by Django 4.0.5 on 2022-06-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getlyrics', '0004_songlyricstest_song_artist_songlyricstest_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlyricstest',
            name='song_artist',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AlterField(
            model_name='songlyricstest',
            name='song_title',
            field=models.CharField(default=None, max_length=5000),
        ),
    ]