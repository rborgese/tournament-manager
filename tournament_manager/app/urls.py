from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('teams/', views.teams, name='teams'),
    path('groups/', views.groups, name='groups'),
    path('knockouts/', views.knockouts, name='knockouts'),
    path('matches/', views.teams, name='matches'),
    path('settings/', views.settings, name='settings'),
]
