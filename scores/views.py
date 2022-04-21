from .models import Score
from .serializers import ScoreSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from jwt_auth.serializers import UserSerializer 

# Listing leagues
# Creating leagues
class ScoreList(ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class AllocateDailyScore(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    AddScore = Score.objects.get(pk=pk)

    print('ALERT', AddScore, pk)
    
