#ici la base de donnee generale, utilisee par toutes les vues
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import datetime,date

#Create your models here
class Utilisateur(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default='',related_name='profile')
	dateNaissance= models.DateField("Date de naissance",default=date.today)
	photo = models.ImageField(upload_to="photos/",default='cat.jpg')
	sexe= models.CharField(max_length=6,
                           choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female'),
                                )
                           )
	tel= models.CharField(max_length=12)#voir pour changer avec des forms (pour ne pas pouvoir mettre de num absurde)
	def __str__(self):
        	return "Profil de {0}".format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Utilisateur.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Sport(models.Model):
	photo = models.ImageField(upload_to="photoSports/",default='photoSports/cap.jpeg')
	nom= models.CharField(max_length=20)
	def __str__(self):
        	return self.nom


class Evenement(models.Model):
    titre= models.CharField(max_length=20,null=True)
    sports=models.ForeignKey(Sport, on_delete=models.CASCADE,default=None) #ManyToManyField permet relation plusieurs a plusieurs (ce qu'on veut ici, un evenement peut avoir +sieurs sport et un sport peut etre affilie a +sieurs evts)
    date=models.DateField("Date événement",default=datetime.now())
    heure=models.CharField(max_length=20,default="Heure indéfinie")
    createur=models.ForeignKey(User, on_delete=models.CASCADE)
    nbPlaces= models.IntegerField("Nombre de places")
    placesRestantes=models.IntegerField("Nombre de places restantes",default=0)
    description= models.TextField()
    photoEvt=models.ImageField("Photo de l'événement",upload_to="photoEvt/",default='photoEvt/evtbase.png')

class Adherence(models.Model):
    adherent=models.ForeignKey(User, on_delete=models.CASCADE)
    sport=models.ForeignKey(Sport, on_delete=models.CASCADE)

class Participation(models.Model):
    participant=models.ForeignKey(User, on_delete=models.CASCADE)
    evenement= models.ForeignKey(Evenement, on_delete=models.CASCADE)
    participe=models.CharField(max_length=8,
    							choices=(
    								('-1','pas croise'),
    								('0','Oui'),
    								('1','Non'),
    								),
    							default='-1'
    	)
