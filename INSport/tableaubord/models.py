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
    #photoProfil= models.ImageField(upload_to="photosProfil/",default="photosProfil/profil.jpeg")  #cf settings.py, on a defini comme racine de mediapath deploment/media

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Utilisateur.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Sport(models.Model):
    #photoSport=  models.ImageField(upload_to="photosSport/")
    nom= models.CharField(max_length=20)

class Evenement(models.Model):
    sports=models.ManyToManyField(Sport) #ManyToManyField permet relation plusieurs a plusieurs (ce qu'on veut ici, un evenement peut avoir +sieurs sport et un sport peut etre affilie a +sieurs evts)
    dateheure=  models.DateTimeField('Date/heure evenement ',default=datetime.now())
    createur=models.ForeignKey(User, on_delete=models.CASCADE)
    nbPlaces= models.IntegerField()
    description= models.CharField(max_length=250)
    #photoEvt=models.ImageField(upload_to="photosEvt/")

class Adherence(models.Model):
    adherent=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    sport=models.ForeignKey(Sport, on_delete=models.CASCADE)

class Participation:
    participant=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement= models.ForeignKey(Evenement, on_delete=models.CASCADE)
