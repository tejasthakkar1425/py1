from django import forms
from django.forms import fields
from home.models import *

class Gst(forms.ModelForm):
    class Meta:
        model=Gstcharges
        fields="__all__"