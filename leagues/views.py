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


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")