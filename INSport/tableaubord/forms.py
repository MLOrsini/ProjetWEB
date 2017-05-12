from django import forms
from django import forms
from .models import Utilisateur, Evenement
from django.contrib.auth.models import User

class UtilisateurForm(forms.ModelForm):
	required_css_class = 'required'
	class Meta:
        	model = Utilisateur
        	exclude = ('user',) 

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email','username','password')
		password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
		widgets = {
			    'password': forms.PasswordInput(),
			}
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("That user is already taken")
		return username



class createEventForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'

