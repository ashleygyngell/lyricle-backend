# Generated by Django 4.0.4 on 2022-04-21 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_alter_score_daily_correct_in_1_and_more'),
        ('dailysongs', '0002_alter_song_song_clue_1_alter_song_song_clue_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_clue_5',
        ),
        migrations.AddField(
            model_name='song',
            name='daily_song_stats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='song_scores', to='scores.score'),
        ),
    ]
