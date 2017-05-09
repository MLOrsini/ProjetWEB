from django import forms
from django import forms
from .models import Utilisateur
from django.contrib.auth.models import User

class UtilisateurForm(forms.ModelForm):
	required_css_class = 'required'
	class Meta:
        	model = Utilisateur
        	exclude = ('user',) 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password',)
