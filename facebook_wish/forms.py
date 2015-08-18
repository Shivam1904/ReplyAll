from django import forms

class NameForm(forms.Form):
    msg = forms.CharField(label='Thanks :)')