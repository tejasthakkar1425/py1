from django import forms
from django.forms import fields
from home.models import *

class Gst(forms.ModelForm):
    class Meta:
        model=Gstcharges
        fields="__all__"


class DisForm(forms.ModelForm):
    class Meta:
        model = DistrictMaster
        fields = ('district_id','district_name','state','description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
            'class': "mt-1 form-input", 
            }
        self.fields['district_id'].widget.attrs['required'] = True
        self.fields['district_name'].widget.attrs['required'] = True
        self.fields['state'].widget.attrs['required'] = True
        self.fields['description'].widget.attrs['required'] = True
