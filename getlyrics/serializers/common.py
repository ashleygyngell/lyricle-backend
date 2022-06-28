from rest_framework import serializers
from ..models import *


# This class controls how a Song is serialized to JSON. Is inherited from the default Model Serializer 
class SongLyricSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = SongLyricsTest
    # Which fields to serialize 
    fields = ('song_title', 'song_artist')
