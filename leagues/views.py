from .models import League
from .serializers.common import LeagueSerializer # get the League Serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

# Listing leagues
# Creating leagues
class LeagueList(ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
