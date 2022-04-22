from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('joinleague/<int:pk>/', JoinLeague.as_view()),
    path('addscore/<int:pk>/', AllocateDailyScoreIn1.as_view()),
]