# Generated by Django 4.0.4 on 2022-04-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0019_remove_customuser_user_leagues_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.CharField(max_length=10),
        ),
    ]
