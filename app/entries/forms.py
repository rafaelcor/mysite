from django import forms
from entries.models import Entry





class RegristryForm(forms.Form):
    ent2 = forms.CharField(widget=forms.Textarea(attrs={'id': 'ent2',
                                                        'class': 'ent2', }))
