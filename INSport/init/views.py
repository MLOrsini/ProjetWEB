from django.shortcuts import render
from tableaubord.models import Sport
# Create your views here.

def init(request):

	#en premier lieu on clean
	sports=Sport.objects.all()
	for sport in sports:
		sport.delete()

	cap=Sport(nom="Course a pied",photo='photoSports/running.png')
	cap.save()

	nat=Sport(nom="Natation",photo='photoSports/nat.png')
	nat.save()

	muscu=Sport(nom="Musculation",photo='photoSports/muscu.png')
	muscu.save()

	velo=Sport(nom="Vélo",photo='photoSports/velo.png')
	velo.save()

	tennis=Sport(nom="Tennis",photo='photoSports/tennis.png')
	tennis.save()

	pingpong=Sport(nom="Tennis de table",photo='photoSports/ping-pong.png')
	pingpong.save()

	arc=Sport(nom="Tir a l'arc",photo='photoSports/archery.png')
	arc.save()

	foot=Sport(nom="Football",photo='photoSports/football.png')
	foot.save()

	rugby=Sport(nom="Rugby",photo='photoSports/rugby.png')
	rugby.save()

	grimpe=Sport(nom="Escalade",photo='photoSports/escalade.png')
	grimpe.save()

	wtf=Sport(nom="Sports de combat",photo='photoSports/boxing.png')
	wtf.save()

	squash=Sport(nom="Squash",photo='photoSports/squash.png')
	squash.save()

	bad=Sport(nom="Badminton",photo='photoSports/bad.png')
	bad.save()

	curling=Sport(nom="Curling",photo='photoSports/curling.png')
	curling.save()

	volley=Sport(nom="Volleyball",photo='photoSports/volleyball.png')
	volley.save()

	sports=Sport.objects.all()
	return render(request, 'init.html',{'sports':sports})
