from rest_framework import serializers
from ..models import Song


# This class controls how a Song is serialized to JSON. Is inherited from the default Model Serializer 
class SongSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = Song
    # Which fields to serialize 
    fields = ('__all__')

