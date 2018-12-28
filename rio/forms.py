from django import forms

from .models import Oder

class OderForm(forms.ModelForm):

    class Meta:
        model = Oder
        fields = ('items','quontity', 'note')
