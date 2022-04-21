from django.db import models
from django.contrib.auth.models import AbstractUser
from scores.models import Score
# from leagues.models import League

# Create your models here.

EMOJI_CHOICE = (
  ('🐶', 'DOG'),
  ('🐱', 'CAT'),
  ('🐭', 'MOUSE'),
  ('🐰', 'BUNNY'),
  # ('🦊', 'FOX'),
  # ('🐻', 'BEAR'),
  # ('🐼', 'PANDA'),
  # ('🐨', 'KOALA'),
  # ('🐯', 'LION'),
  # ('🐮', 'COW'),
  # ('🐷', 'PIG'),
  # ('🐸', 'FROG'),
  # ('🐵', 'MONKEY'),
  # ('🐥', 'CHICK'),
  # ('🦉', 'OWL'),
  # ('🦄', 'UNICORN')
)

class CustomUser(AbstractUser):
    # custom fields here…*
    image = models.CharField(max_length=10, choices=EMOJI_CHOICE, blank=False)
    correct_in_1 = models.IntegerField(blank=True, null=True)
    correct_in_2 = models.IntegerField(blank=True, null=True)
    correct_in_3 = models.IntegerField(blank=True, null=True)
    correct_in_4 = models.IntegerField(blank=True, null=True)
    correct_in_5 = models.IntegerField(blank=True, null=True)
    user_avg = models.FloatField(blank=True, null=True)
    user_leagues = models.ManyToManyField('leagues.League', related_name='UserLeagues', default=None)
    daily_song_stats = models.ForeignKey(Score, related_name='user_daily_score_on_song', on_delete=models.CASCADE, null=True)




    # city = models.ForeignKey('coopcreator.OperationalCity', related_name='user', on_delete=models.SET_NULL , null=True)

        # user_leagues = models.ForeignKey(League, related_name="users_league", max_length=10000, blank=False, on_delete=models.PROTECT)