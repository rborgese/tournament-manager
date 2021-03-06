# Generated by Django 2.2.2 on 2019-06-28 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190628_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='notes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TournamentNote'),
        ),
    ]
