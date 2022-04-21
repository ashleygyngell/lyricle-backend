from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('joinleague/<int:pk>/', JoinLeague.as_view()),
    path('viewscore/<int:pk>/', ViewScores.as_view())
]