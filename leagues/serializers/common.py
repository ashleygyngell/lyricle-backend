from rest_framework import serializers
from ..models import League

# This class controls how a League is serialized to JSON. Is inherited from the default Model Serializer 
class LeagueSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = League
    # Which fields to serialize 
    fields = ('__all__')