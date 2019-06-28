# Generated by Django 2.2.2 on 2019-06-27 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_group_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teams',
        ),
        migrations.AddField(
            model_name='team',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='app.Group'),
        ),
    ]
