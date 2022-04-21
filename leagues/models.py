from pickle import TRUE
from django.db import models

from dailysongs.models import Song
from jwt_auth.serializers import User
from jwt_auth.models import CustomUser
# Create your models here.

#  Defines League Model


class League(models.Model):
    league_id = models.AutoField(auto_created=True,
            primary_key=True,
            serialize=False,
            verbose_name='ID'
            )
    league_name = models.CharField(max_length=50, unique=True)
    daily_songs = models.ManyToManyField(Song, related_name="LeaguesDailySong", default=None)
    # league_users = models.ManyToManyField(User, related_name="UserLLeagues", default=None)

    def __str__(self):
        return self.league_name

