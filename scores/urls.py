from django.urls import path
from .views import *

urlpatterns = [
    path('', ScoreList.as_view()),
    path('<int:pk>/', ScoreDetail.as_view())
]