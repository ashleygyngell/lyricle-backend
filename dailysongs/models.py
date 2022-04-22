from django.db import models
from scores.models import Score

# Create your models here.

#  Defines League Model


class Song(models.Model):
    song_id = models.AutoField(auto_created=True,
            primary_key=True,
            serialize=False,
            verbose_name='ID'
            )
    song_title = models.CharField(max_length=50)
    song_clue_1 = models.CharField(max_length=300)
    song_clue_2 = models.CharField(max_length=300)
    song_clue_3 = models.CharField(max_length=300)
    song_clue_4 = models.CharField(max_length=300)
    daily_song_stats = models.ForeignKey(Score, related_name='song_scores', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.song_title

  

