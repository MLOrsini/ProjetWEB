from django import forms
from django import forms
from .models import Utilisateur

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'
