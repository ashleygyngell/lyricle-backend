# Generated by Django 4.0.4 on 2022-04-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0006_league_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='code',
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
