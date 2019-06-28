from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse

from .models import Group, Team, Tournament, Knockout


# Create your views here.
def index(request):
    context = {}
    return render(request, "app/index.html", context={})


def tournaments(request):
    return HttpResponse("The tournaments page")


def groups(request):
    """
    Displays the groups and each particular groups leaderboard and matches.

    :param request:
    :return:
    """
    tournament = Tournament.objects.get(pk=1)
    groups = Group.objects.all()
    context = {'groups': groups, 'tournament': tournament}
    return render(request, 'app/groups.html', context=context)


def knockouts(request):
    """
    Displays the knockouts and matches.

    :param request:
    :return:
    """
    tournament = Tournament.objects.get(pk=1)
    knockouts = Knockout.objects.all()
    context = {'knockouts': knockouts, 'tournament': tournament}
    return render(request, 'app/knockouts.html', context=context)



def teams(request):
    context = {}
    return HttpResponse("The teams Page")


def matches(request):
    return HttpResponse("The matches Page")


def settings(request):
    return HttpResponse("The settings page")
