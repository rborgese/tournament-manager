# Generated by Django 2.2.2 on 2019-06-28 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190628_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentnote',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='app.Tournament'),
        ),
    ]
