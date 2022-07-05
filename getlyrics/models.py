from django.db import models
from rest_framework.response import Response
import lyricsgenius

LyricsGenius = lyricsgenius.Genius("4wX_AIcVI8fQHIbkWY8z95hKj_23o_04j8FOVD79b-1g_m2GXuYzyfC7pHRDoacU")

# Create your models here.


# class SongLyrics(models.Model):

#     song_lyrics = models.CharField(max_length=30000)
   
#     def __str__(self):
#         return self.song_lyric

class SongLyricsTest(models.Model):
  song = LyricsGenius.search_song("", "")
  song_title = models.CharField(max_length=5000, default=None )
  song_artist = models.CharField(max_length=5000, default=None )
  # print(song.lyrics)
  def __str__(self):
        return self.song_title



# song.save_lyrics(extension='txt')

# artist = LyricsGenius.search_artist("ADELE", max_songs=1)
# artist.songs
# for song in artist.songs:
#     print(song)

# song = LyricsGenius.search_song("Love Yourself", "Bieber")
# print(song.lyrics)

# https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/08-Collect-Genius-Lyrics.html#save-lyrics-to-txt-file



