# Generated by Django 4.0.4 on 2022-04-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_correct_in_1', models.IntegerField(blank=True, null=True)),
                ('daily_correct_in_2', models.IntegerField(blank=True, null=True)),
                ('daily_correct_in_3', models.IntegerField(blank=True, null=True)),
                ('daily_correct_in_4', models.IntegerField(blank=True, null=True)),
                ('daily_correct_in_5', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
