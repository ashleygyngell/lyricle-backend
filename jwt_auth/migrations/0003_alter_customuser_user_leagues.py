# Generated by Django 4.0.4 on 2022-04-20 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_league_league_users'),
        ('jwt_auth', '0002_alter_customuser_user_leagues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_leagues',
            field=models.ForeignKey(max_length=10000, on_delete=django.db.models.deletion.PROTECT, related_name='users_league', to='leagues.league'),
        ),
    ]
