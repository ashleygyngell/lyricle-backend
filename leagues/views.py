from .models import League
from .serializers.common import LeagueSerializer, UserLeagueSerializer # get the League Serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# Listing leagues
# Creating leagues
class LeagueList(ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class LeagueDetail(RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class UserLeague(APIView):
    permission_classes = [ IsAuthenticated ]
    # Get Author by ID - pk is the primary key, passed through our <int:pk> route in urls.py
    def get(self, request):
         # Call the get_author function which will either get the author or raise a HTTP 404 status code response if not present
        user_id = request.user.id
        request.user.user_leagues
        serialized_leagues = UserLeagueSerializer(request.user.user_leagues, many=True)


         # Return the serialized author data and a HTTP 200 response
        return Response(data = serialized_leagues.data, status=200)
