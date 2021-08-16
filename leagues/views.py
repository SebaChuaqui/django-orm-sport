from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker


def index(request):
    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        "consulta1": League.objects.filter(name__contains="Baseball"),
        "consulta2": League.objects.filter(name__contains="Womens"),
        "consulta3": League.objects.filter(name__contains="Hockey"),
        "consulta4": League.objects.exclude(name__contains="Football"),
        "consulta5": League.objects.filter(name__contains="Conference"),
        "consulta6": League.objects.filter(name__contains="Atlantic"),
        "consulta7": Team.objects.filter(location__contains="Dallas"),
        "consulta8": Team.objects.filter(team_name__contains="Raptors"),
        "consulta9": Team.objects.filter(location__contains="City"),
        "consulta10": Team.objects.filter(team_name__startswith="T"),
        "consulta11": Team.objects.order_by('location'),
        "consulta12": Team.objects.order_by('-team_name'),
        "consulta13": Player.objects.filter(last_name__contains="Cooper"),
        "consulta14": Player.objects.filter(first_name__contains="Joshua"),
        "consulta15": Player.objects.filter(last_name__contains="Cooper").exclude(first_name="Joshua"),
        "consulta16": Player.objects.filter(first_name__in=["Alexander", "Wyatt"])

    }
    return render(request, "leagues/index.html", context)


def index2(request):
    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        "consulta1": Team.objects.filter(league__name='Atlantic Soccer Conference'),
        "consulta2": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),
        "consulta3": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
        "consulta4": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),
        "consulta5": Player.objects.filter(curr_team__league__sport="Football"),
        "consulta6": Team.objects.filter(curr_players__first_name="Sophia"),
        "consulta7": League.objects.filter(teams__curr_players__first_name="Sophia"),
        "consulta8": Player.objects.exclude(curr_team__team_name="Roughriders", curr_team__location="Washington").filter(last_name="Flores"),
        "consulta9": Team.objects.filter(all_players__first_name="Samuel") & Team.objects.filter(all_players__last_name="Evans"),
        "consulta10": Player.objects.filter(all_teams__team_name="Tiger-Cats") & Player.objects.filter(all_teams__location="Manitoba"),
        "consulta11": Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings").filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita"),
		"consulta12" : Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),
        "consulta13" : Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players").filter(first_name="Joshua"),
        "consulta14" : Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
        "consulta15" : Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
    }
    return render(request, "leagues/index2.html", context)


def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")
