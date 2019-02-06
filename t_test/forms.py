from django import forms
from .models import TareaNoc

class nuevaTareaForm(forms.ModelForm):

    class Meta():
        model=TareaNoc
        fields='__all__'
