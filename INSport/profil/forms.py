from django import forms
from tableaubord.models import Utilisateur, Adherence, Sport

class UserForm(forms.ModelForm):
    required_css_class = 'required'

    def merge_from_initial(self):
        filt = lambda v: v not in self.data.keys()
        for field in filter(filt, getattr(self.Meta, 'fields', ())):
            self.data[field] = self.initial.get(field, None)
        

    class Meta:
        model = Utilisateur
        exclude = ('user',) # user doit être exclu du formulaire, sinon on pourrait changer les infos d'un autre utilisateur en le sélectionnant!
        widget = forms.PasswordInput(render_value = False)
        

class AdherenceForm(forms.ModelForm):
    class Meta:
        model = Adherence
        fields = '__all__'

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'		
