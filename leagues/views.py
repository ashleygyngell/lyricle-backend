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
   
    def get(self, request):

        user_id = request.user.id
        request.user.user_leagues
        serialized_leagues = UserLeagueSerializer(request.user.user_leagues, many=True)

        return Response(data = serialized_leagues.data, status=200)
