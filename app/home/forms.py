from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'id': 'user_entry'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'id': 'password_entry',
                                                             'type': 'password'}))
