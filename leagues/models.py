from django.db import models

# Create your models here.

#  Defines League Model


class League(models.Model):
    league_id = models.AutoField(auto_created=True,
            primary_key=True,
            serialize=False,
            verbose_name='ID'
            )
    league_name = models.CharField(max_length=50)

    def __str__(self):
        return self.league_name

  

