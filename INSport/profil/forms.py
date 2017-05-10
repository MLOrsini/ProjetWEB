from django import forms
from tableaubord.models import Utilisateur, Adherence, Sport

class UserForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class AdherenceForm(forms.ModelForm):
    class Meta:
        model = Adherence
        fields = '__all__'

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'		
