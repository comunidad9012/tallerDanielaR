from pyexpat import model
from socket import fromshare
from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'