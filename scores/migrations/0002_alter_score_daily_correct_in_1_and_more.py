# Generated by Django 4.0.4 on 2022-04-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='daily_correct_in_1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='daily_correct_in_2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='daily_correct_in_3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='daily_correct_in_4',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='daily_correct_in_5',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
