from rest_framework import serializers
from .models import Score
from dailysongs.models import Song
from dailysongs.serializers.common import SongSerializer
from jwt_auth.serializers import UserSerializer
# This class controls how a Score is serialized to JSON. Is inherited from the default Model Serializer 
class ScoreSerializer(serializers.ModelSerializer):


  class Meta:
 # The class type we want it to serialize
    model = Score
    # Which fields to serialize 
    fields = ('__all__')

class MultipleScoreSerializer(serializers.ModelSerializer):

  scores = ScoreSerializer(many=True)

class AddDailyScoreSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = Song

    daily_song_stats = SongSerializer(many=True) 
    # Which fields to serialize 
    fields = ('daily_song_stats',)
