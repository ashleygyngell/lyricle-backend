import lyricsgenius
LyricsGenius = lyricsgenius.Genius("4wX_AIcVI8fQHIbkWY8z95hKj_23o_04j8FOVD79b-1g_m2GXuYzyfC7pHRDoacU")

song = LyricsGenius.search_song("Loyalty", "Kendrik Lamar")
print(song.lyrics)
# song.save_lyrics(extension='txt')

# artist = LyricsGenius.search_artist("ADELE", max_songs=1)
# artist.songs
# for song in artist.songs:
#     print(song)

# song = LyricsGenius.search_song("Love Yourself", "Bieber")
# print(song.lyrics)

# https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/08-Collect-Genius-Lyrics.html#save-lyrics-to-txt-file

from rest_framework.response import Response