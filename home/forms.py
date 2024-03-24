from django import forms
from django.forms import fields
from home.models import *

class Gst(forms.ModelForm):
    class Meta:
        model=Gstcharges
        fields="__all__"


class DisForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
        super(DisForm, self).__init__(*args, **kwargs)
        self.fields['state'].choices = [(obj.state_id, obj.stat_name) for obj in StateMasterTable.objects.all()]
      class Meta:
        model = DistrictMaster
        fields = '__all__'
        fields = ['district_id', 'district_name','state','description']
        labels = {
            'district_id': 'district ID',
            'district_name' : 'District Name',
            'state' : 'State Name.' ,
            'description' : 'Description'
        }
