from rest_framework import serializers

from jwt_auth.serializers import UserSerializer
from ..models import League

# This class controls how a League is serialized to JSON. Is inherited from the default Model Serializer 
class JoinLeagueSerializer(serializers.ModelSerializer):

  class Meta:
 # The class type we want it to serialize
    model = League

    league_users = UserSerializer(many=True) 
    # Which fields to serialize 
    fields = ('league_users',)

class LeagueSerializer(serializers.ModelSerializer):

   class Meta:
 # The class type we want it to serialize
    model = League

    league_users = UserSerializer(many=True) 
    # Which fields to serialize 
    fields = ('league_name', 'league_users', 'daily_songs' )

class UserLeagueSerializer(serializers.ModelSerializer):

    class Meta: 

     model = League

     league_users = UserSerializer(many=True) 

     fields = ('league_name', 'league_users')