# Generated by Django 4.0.4 on 2022-04-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0006_remove_customuser_user_leagues_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_leagues',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.CharField(choices=[('🐶', 'DOG'), ('🐱', 'CAT'), ('🐭', 'MOUSE'), ('🐰', 'BUNNY')], max_length=10),
        ),
    ]