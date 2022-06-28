from email import message
from .models import SongLyricsTest
from .serializers.common import SongLyricSerializer # get the Song Serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import lyricsgenius

LyricsGenius = lyricsgenius.Genius("4wX_AIcVI8fQHIbkWY8z95hKj_23o_04j8FOVD79b-1g_m2GXuYzyfC7pHRDoacU")

# Listing Songs
# Creating Songs
class getLyrics(APIView):
  
    def post(self, request):
        # serializer = SongLyricSerializer(data=request.data)
        # if serializer.is_valid():
          
          serialized_songs = SongLyricSerializer(request)
          song_title = request.data.get('song_title')
          song_artist = request.data.get('song_artist')
          print('HERE IT IS: ', song_title)
          data = LyricsGenius.search_song(f'{song_title}, {song_artist}')
        #  data = LyricsGenius.search_song(f'{serializer}, {serializer}')
        # print(data.lyrics)

          lyrics = data.lyrics
          def __str__(self):
            return self.data

          return Response(lyrics, status=200)

# class getLyrics(ListCreateAPIView):
#     queryset = SongLyricsTest.objects.all()
#     serializer_class = SongLyricSerializer
  
    
#     def get(request, null):
        
        
#         serialized_songs = SongLyricSerializer(request)
#         data = LyricsGenius.search_song("DNA", "Kendrik Lamar")
#         # print(data.lyrics)
#         lyrics = data.lyrics
#         def __str__(self):
#           return self.data

#         return Response(lyrics, status=200)





