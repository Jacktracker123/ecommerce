from django import forms
from . models import *
class Phone_form(forms.Form):
    name=forms.CharField(max_length=500)
    image=forms.CharField(max_length=3000)
    price=forms.CharField(max_length=500)

class Computer_form(forms.ModelForm):
    class Meta:
        model=Computer
        fields='__all__'