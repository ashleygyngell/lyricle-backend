from django.urls import path
from .views import *

urlpatterns = [
    path('', LeagueList.as_view()),
    path('<int:pk>/', LeagueDetail.as_view()),
    path('userleagues/', UserLeague.as_view()),
    # path('createleagues/', CreateLeague.as_view()),
]