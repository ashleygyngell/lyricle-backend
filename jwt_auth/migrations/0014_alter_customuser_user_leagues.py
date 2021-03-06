# Generated by Django 4.0.4 on 2022-04-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_remove_league_league_users'),
        ('jwt_auth', '0013_alter_customuser_correct_in_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_leagues',
            field=models.ManyToManyField(default=None, related_name='league_users', to='leagues.league'),
        ),
    ]
