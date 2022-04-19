from .models import Song
from .serializers.common import SongSerializer # get the Song Serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

# Listing Songs
# Creating Songs
class SongList(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
