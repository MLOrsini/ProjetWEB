from django import forms
from tableaubord.models import Utilisateur, Adherence, Sport, Evenement


class EventForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'		
