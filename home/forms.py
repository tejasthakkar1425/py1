from typing import Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import fields
from django.forms.utils import ErrorList
from home.models import *

class Gst(forms.ModelForm):
    class Meta:
        model=Gstcharges
        fields="__all__"

class stateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(stateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = StateMasterTable
        fields ='__all__'
        fields = ['state_id', 'stat_name','description']
        labels = {
            'state_id': 'State id',
            'stat_name' : 'State Name',
            'description' : 'Description',
        } 

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

class cityVilageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(cityVilageForm, self).__init__(*args, **kwargs)
        self.fields['district'].choices = [(obj.district_id, obj.district_name) for obj in DistrictMaster.objects.all()]
        self.fields['state'].choices = [(obj.state_id, obj.stat_name) for obj in StateMasterTable.objects.all()]
    class Meta:
        model = CityVillageMaster
        fields = '__all__'
        fields = ['city_village_id', 'district','state','city_village_name','description']
        labels = {
            'city_village_id': 'CITY VILLAGE ID',
            'district' : 'DISTRICT NAME',
            'state' : 'STATE NAME' ,
            'city_village_name':'CITY / VILLAGE NAME',
            'description' : 'DESCRIPTION'
        }