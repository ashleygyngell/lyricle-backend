# Generated by Django 4.0.4 on 2022-04-20 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_league_league_users'),
        ('jwt_auth', '0005_remove_customuser_user_leagues_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_leagues',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_leagues',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users_league', to='leagues.league'),
        ),
    ]
