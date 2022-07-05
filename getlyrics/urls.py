from django.urls import path
from .views import *

urlpatterns = [
    path('', getLyrics.as_view()),

]
