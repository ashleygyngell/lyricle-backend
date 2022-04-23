from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
from leagues.models import League
from scores.models import Score
from dailysongs.models import Song
import jwt
from .serializers import UserSerializer 
from leagues.serializers.common import JoinLeagueSerializer
from scores.serializers import AddDailyScoreSerializer
User = get_user_model()

# To Register a User
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)

# To Login 
class LoginView(APIView):

    def get_user(self, email):

        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})

# To see Users information
class CredentialsView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# To Join a League
class JoinLeague(APIView):
  permission_classes = [IsAuthenticated,]
  
  def put(self, request, pk):
   leagueToJoin = League.objects.get(pk=pk)

   print('ALERT',leagueToJoin)
   request.data['league_users'] = [(leagueToJoin.league_users.add(request.user.id))]

   Join_LeagueSerializer = JoinLeagueSerializer(leagueToJoin, data=request.data)
  
   if Join_LeagueSerializer.is_valid():

            Join_LeagueSerializer.save()

            return Response(data=Join_LeagueSerializer.data, status=status.HTTP_201_CREATED)

   return Response(data=Join_LeagueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllocateDailyScoreIn1(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    leagueId = request.GET.get("leagueId")
    
    
    league = League.objects.get(pk=leagueId)
    daily_song = Song.objects.get(pk=pk)
   
    Score.objects.get_or_create(daily_correct_in_1 = request.user, daily_song = daily_song, league = league)
    # addScoreIn1ToSong.daily_correct_in_1 = request.user
    # addScoreIn1ToSong.get_or_create()
    return Response(status=status.HTTP_201_CREATED)
    # print('THISISTHESONG', addScoreIn1ToSong, 'THE USER', request.user.id, )
    # request.data['daily_correct_in_1'] = request.user

    # add_dailyscore = AddDailyScoreSerializer(addScoreIn1ToSong, data=request.data)

    # if add_dailyscore.is_valid():

    #         add_dailyscore.save()

    #         return Response(data=add_dailyscore.data, status=status.HTTP_201_CREATED)

    # return Response(data=add_dailyscore.errors, status=status.HTTP_400_BAD_REQUEST)

class AllocateDailyScoreIn2(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    leagueId = request.GET.get("leagueId")
    
    
    league = League.objects.get(pk=leagueId)
    daily_song = Song.objects.get(pk=pk)
   
    Score.objects.get_or_create(daily_correct_in_2 = request.user, daily_song = daily_song, league = league)
    # addScoreIn1ToSong.daily_correct_in_1 = request.user
    # addScoreIn1ToSong.get_or_create()
    return Response(status=status.HTTP_201_CREATED)

class AllocateDailyScoreIn3(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    leagueId = request.GET.get("leagueId")
    
    
    league = League.objects.get(pk=leagueId)
    daily_song = Song.objects.get(pk=pk)
   
    Score.objects.get_or_create(daily_correct_in_3 = request.user, daily_song = daily_song, league = league)
    # addScoreIn1ToSong.daily_correct_in_1 = request.user
    # addScoreIn1ToSong.get_or_create()
    return Response(status=status.HTTP_201_CREATED)

class AllocateDailyScoreIn4(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    leagueId = request.GET.get("leagueId")
    
    
    league = League.objects.get(pk=leagueId)
    daily_song = Song.objects.get(pk=pk)
   
    Score.objects.get_or_create(daily_correct_in_4 = request.user, daily_song = daily_song, league = league)
    # addScoreIn1ToSong.daily_correct_in_1 = request.user
    # addScoreIn1ToSong.get_or_create()
    return Response(status=status.HTTP_201_CREATED)

class AllocateDailyScoreIn5(APIView): 
  permission_classes = [IsAuthenticated,]

  def put(self, request, pk):
    leagueId = request.GET.get("leagueId")
    
    
    league = League.objects.get(pk=leagueId)
    daily_song = Song.objects.get(pk=pk)
   
    Score.objects.get_or_create(daily_correct_in_5 = request.user, daily_song = daily_song, league = league)
    # addScoreIn1ToSong.daily_correct_in_1 = request.user
    # addScoreIn1ToSong.get_or_create()
    return Response(status=status.HTTP_201_CREATED)

  
  