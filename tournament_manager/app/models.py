from django.db import models


# Create your models here.
from django.db.models import Sum, F
from django.db.models.functions import Coalesce


class Group(models.Model):
    """
    A tournament 'group'. A group will contain a set of teams and matches.
    """
    name = models.CharField(max_length=100)
    
    @property
    def sorted_teams(self):
        return enumerate(sorted(self.teams.all(), key=lambda t: (t.points, t.goal_difference), reverse=True), start=1)

    def __str__(self):
        return f"{self.name}"


class Knockout(models.Model):
    """
    A tournament 'knockout'. A knockout will contain a set of matches
    """
    name = models.CharField(max_length=100)

    @property
    def enumerated_matches(self):
        return enumerate(self.matches.all(), start=1)

    # @property
    # def sorted_teams(self):
    #     return enumerate(sorted(self.teams.all(), key=lambda t: (t.points, t.goal_difference), reverse=True), start=1)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    has_paid = models.BooleanField(default=False)

    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='teams', null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def games_played(self):
        return self.home_matches.count() + self.away_matches.count()

    @property
    def goals_for(self):
        home_goals = self.home_matches.aggregate(sum=Coalesce(Sum('home_goals'), 0))
        away_goals = self.away_matches.aggregate(sum=Coalesce(Sum('away_goals'), 0))
        return home_goals['sum'] + away_goals['sum']

    @property
    def goals_against(self):
        home_goals_conceeded = self.home_matches.aggregate(sum=Coalesce(Sum('away_goals'), 0))
        away_goals_conceeded = self.away_matches.aggregate(sum=Coalesce(Sum('home_goals'), 0))
        return home_goals_conceeded['sum'] + away_goals_conceeded['sum']

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    @property
    def wins(self):
        home_wins = self.home_matches.filter(home_goals__gt=F('away_goals')).count()
        away_wins = self.away_matches.filter(away_goals__gt=F('home_goals')).count()
        return home_wins + away_wins

    @property
    def losses(self):
        home_losses = self.home_matches.filter(home_goals__lt=F('away_goals')).count()
        away_losses = self.away_matches.filter(away_goals__lt=F('home_goals')).count()
        return home_losses + away_losses

    @property
    def draws(self):
        home_draws = self.home_matches.filter(home_goals=F('away_goals')).count()
        away_draws = self.away_matches.filter(away_goals=F('home_goals')).count()
        return home_draws + away_draws

    @property
    def points(self):
        """
        Return the total points total
        :return:
        """
        return self.wins * 3 + self.draws * 1


class Match(models.Model):
    """
    A football match. Can be won, lost or drawn.
    """
    # Can be either in a group stage or a knockout stage
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='matches', blank=True)
    knockout = models.ForeignKey(Knockout, on_delete=models.SET_NULL, null=True, related_name='matches', blank=True)

    time = models.DateTimeField()
    pitch = models.IntegerField()

    is_placeholder = models.BooleanField(default=False)
    home_team_placeholder = models.CharField(max_length=100, default='', blank=True, null=True)
    away_team_placeholder = models.CharField(max_length=100, default='', blank=True, null=True)

    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='home_matches', null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='away_matches', null=True, blank=True)

    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)

    @property
    def is_home_win(self):
        return self.home_goals > self.away_goals

    @property
    def is_away_win(self):
        return self.away_goals > self.home_goals

    def __str__(self):
        if not self.home_team or not self.away_team:
            return 'TBC'
        return f"{self.home_team.name} vs {self.away_team.name}"


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    extra_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} @ {self.location}"


class TournamentNote(models.Model):
    content = models.TextField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")

    def __str__(self):
        return f"{self.tournament.name} : {self.content}"
