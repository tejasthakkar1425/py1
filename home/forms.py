from django import forms
from django.forms import fields
from home.models import *

class Gst(forms.ModelForm):
    class Meta:
        model=Gstcharges
        fields="__all__"

class DisForm(forms.ModelForm):
    district_id = models.IntegerField(primary_key=True)
    district_name = models.TextField(blank=True, null=True)
    state = models.ForeignKey('StateMasterTable',on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50)
    created_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='districtmaster_updated_by_user_set', blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)