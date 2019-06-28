# Generated by Django 2.2.2 on 2019-06-28 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190628_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='notes',
        ),
        migrations.AddField(
            model_name='tournamentnote',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tournament'),
        ),
    ]