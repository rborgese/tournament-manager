# Generated by Django 2.2.2 on 2019-06-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_tournament_extra_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_team_placeholder',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_placeholder',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
