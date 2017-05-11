from django import forms
from tableaubord.models import Utilisateur, Adherence, Sport

class UserForm(forms.ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Utilisateur
		exclude = ('user',) # user doit être exclu du formulaire, sinon on pourrait changer les infos d'un autre utilisateur en le sélectionnant!

class AdherenceForm(forms.ModelForm):
    class Meta:
        model = Adherence
        fields = '__all__'

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'		
