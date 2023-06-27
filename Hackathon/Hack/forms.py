from django import forms
from Hack.models import Hacka,User

class HackathonRegistrationForm(forms.ModelForm):
    class Meta:
        model = Hacka
        fields = "__all__"

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = "__all__"
