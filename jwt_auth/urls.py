from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('joinleague/<int:pk>/', JoinLeague.as_view()),
    path('addscore1/<int:pk>/', AllocateDailyScoreIn1.as_view()),
    path('addscore2/<int:pk>/', AllocateDailyScoreIn2.as_view()),
    path('addscore3/<int:pk>/', AllocateDailyScoreIn3.as_view()),
    path('addscore4/<int:pk>/', AllocateDailyScoreIn4.as_view()),
    path('addscore5/<int:pk>/', AllocateDailyScoreIn5.as_view()),
]