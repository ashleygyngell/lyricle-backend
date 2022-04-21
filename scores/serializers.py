from rest_framework import serializers
from .models import Score
from jwt_auth.models import CustomUser
# This class controls how a League is serialized to JSON. Is inherited from the default Model Serializer 
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
       model = CustomUser
       fields = ('daily_song_stats',)
