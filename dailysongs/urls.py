from django.urls import path
from .views import *

urlpatterns = [
    path('', SongList.as_view()),
    path('<int:pk>/', SongDetail.as_view())
]