from django.contrib import admin

# Register your models here.
from app.models import Group, Knockout, Team, Match, Tournament


class MatchesInline(admin.TabularInline):
    model = Match


class TeamsInline(admin.TabularInline):
    model = Team
    readonly_fields = ['games_played',
                       'wins',
                       'losses',
                       'draws',
                       'points',
                       ]
    extra = 0



class HomeMatchesInline(admin.TabularInline):
    model = Match
    verbose_name_plural = "Home Matches"
    fk_name = 'home_team'
    extra = 0


class AwayMatchesInline(admin.TabularInline):
    model = Match
    verbose_name_plural = "Away Matches"
    fk_name = 'away_team'
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        TeamsInline,
        MatchesInline,
    ]


class KnockoutAdmin(admin.ModelAdmin):
    inlines = [
        MatchesInline,
    ]



class TeamAdmin(admin.ModelAdmin):
    inlines = [
        HomeMatchesInline,
        AwayMatchesInline
    ]

    readonly_fields = ['games_played',
                       'wins',
                       'losses',
                       'draws',
                       'goals_for',
                       'goals_against',
                       'goal_difference',
                       'points']


admin.site.register(Tournament)
admin.site.register(Group, GroupAdmin)
admin.site.register(Knockout, KnockoutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match)