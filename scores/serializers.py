from rest_framework import serializers
from .models import Score
# This class controls how a League is serialized to JSON. Is inherited from the default Model Serializer 
class ScoreSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = Score
    # Which fields to serialize 
    fields = ('__all__')

class MultipleScoreSerializer(serializers.ModelSerializer):

  scores = ScoreSerializer(many=True)