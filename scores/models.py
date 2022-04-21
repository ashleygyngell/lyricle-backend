from django.db import models

# Create your models here.

#  Defines League Model


class Score(models.Model):
    daily_song = models.ForeignKey('dailysongs.song', related_name='song1_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    league = models.ForeignKey('leagues.league', related_name='song1_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    daily_correct_in_1 = models.ForeignKey('jwt_auth.CustomUser', related_name='song1_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    daily_correct_in_2 = models.ForeignKey('jwt_auth.CustomUser', related_name='song2_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    daily_correct_in_3 = models.ForeignKey('jwt_auth.CustomUser', related_name='song3_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    daily_correct_in_4 = models.ForeignKey('jwt_auth.CustomUser', related_name='song4_daily_scores', on_delete=models.CASCADE, blank=True, null=True)
    daily_correct_in_5 = models.ForeignKey('jwt_auth.CustomUser', related_name='song5_daily_scores', on_delete=models.CASCADE, blank=True, null=True)

