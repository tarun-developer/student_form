from django import forms
from django.core import validators
# our new form

def check_for_z(value):
    if len(value)>0:
        raise forms.ValidationError("Gotta BOT!")
class FormName(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    