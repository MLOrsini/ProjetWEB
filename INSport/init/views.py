from django.shortcuts import render
from tableaubord.models import Sport
# Create your views here.

def init(request):

	#en premier lieu on clean
	sports=Sport.objects.all()
	for sport in sports:
		sport.delete()

	cap=Sport(id="1")
	cap.nom="Course à pied"
	cap.photo='photoSports/running.png'
	cap.save()

	nat=Sport(id="2")
	nat.nom="Natation"
	nat.photo='photoSports/nat.png'
	nat.save()

	muscu=Sport(id="3")
	muscu.nom="Musculation"
	muscu.photo='photoSports/muscu.png'
	muscu.save()

	velo=Sport(id="4")
	velo.nom="Vélo"
	velo.photo='photoSports/velo.png'
	velo.save()

	tennis=Sport(id="5")
	tennis.nom="Tennis"
	tennis.photo='photoSports/tennis.png'
	tennis.save()

	pingpong=Sport(id="6")
	pingpong.nom="Tennis de table"
	pingpong.photo='photoSports/ping-pong.png'
	pingpong.save()

	arc=Sport(id="7")
	arc.nom="Tir à l'arc"
	arc.photo='photoSports/archery.png'
	arc.save()

	foot=Sport(id="8")
	foot.nom="Football"
	foot.photo='photoSports/football.png'
	foot.save()

	rugby=Sport(id="9")
	rugby.nom="Rugby"
	rugby.photo='photoSports/rugby.png'
	rugby.save()

	grimpe=Sport(id="10")
	grimpe.nom="Escalade"
	grimpe.photo='photoSports/escalade.png'
	grimpe.save()

	wtf=Sport(id="11")
	wtf.nom="Sports de combat"
	wtf.photo='photoSports/boxing.png'
	wtf.save()

	squash=Sport(id="12")
	squash.nom="Squash"
	squash.photo='photoSports/squash.png'
	squash.save()

	bad=Sport(id="13")
	bad.nom="Badminton"
	bad.photo='photoSports/bad.png'
	bad.save()

	curling=Sport(id="14")
	curling.nom="Curling"
	curling.photo='photoSports/curling.png'
	curling.save()

	volley=Sport(id="15")
	volley.nom="Volleyball"
	volley.photo='photoSports/volleyball.png'
	volley.save()


	sports=Sport.objects.all()
	return render(request, 'init.html',{'sports':sports})
