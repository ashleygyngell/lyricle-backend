from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation', 'image', 'user_leagues', 'correct_in_1', 'correct_in_2', 'correct_in_3', 'correct_in_4', 'correct_in_5', 'user_avg',  )


class JoinLeagueSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = User
        fields = ('id', 'league_users')


