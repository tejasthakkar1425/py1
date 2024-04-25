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

class Gstform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Gstform, self).__init__(*args, **kwargs)
    class Meta:
        model=Gstcharges
        fields="__all__"
        fields = ['gst_char_id', 'year','cgst_per','sgst_per']
        labels = {
            'gst_char_id': 'Gst Charges Id',
            'year' : 'Year',
            'cgst_per' : 'Cgst per' ,
            'sgst_per':'Sgst per',
        }

class Userform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
    class Meta:
        model=UserMasterTable
        fields="__all__"
        fields= ['user_master_id', 'user_email_id','user_name','user_password']
        labels = {
            'user_master_id': 'User Id',
            'user_email_id' : 'Email Id',
            'user_name' : 'User Name' ,
            'user_password':'Password',
        }

class Paymentform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Paymentform, self).__init__(*args, **kwargs)
        self.fields['doc'].choices = [(obj.doc_id, obj.doc_number) for obj in DocMaster.objects.all()]
    class Meta:
        model=PaymentMaster
        fields="__all__"
        fields = ['doc_pay_detail', 'doc_pay_detail_id','doc','pay_status','pay_method','pay_tran_id','pay_response']
        labels = {
            'doc_pay_detail': 'Payment Deatils',
            'doc_pay_detail_id' : 'Payment Id',
            'doc' : 'Doc id' ,
            'pay_status':'Payment Status',
            'pay_method': 'Payment Method',
            'pay_tran_id' : 'Transection Id',
            'pay_response' : 'Response',
        }
class Reviewform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Reviewform, self).__init__(*args, **kwargs)
        self.fields['user'].choices = [(obj.user_master_id, obj.user_name) for obj in UserMasterTable.objects.all()]
    class Meta:
        model=ReviewFeedback
        fields= "__all__"
        fields = ['user','review_image','review_description','review_star']
        labels = {
            'user' : 'User Id',
            'review_image' : 'Image',
            'review_description' : 'Description' ,
            'review_star':'Stars',
        }

class Vehicleform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Vehicleform, self).__init__(*args, **kwargs)
    class Meta:
        model=VehicleMaster
        fields="__all__"
        fields= ['vehicle_id', 'vehicle_name','rc_book_number','reg_no','capacity','insurance_from','insurance_to','insurance_company_name','owner_name']
        labels = {
            'vehicle_id': 'Vehicle Id',
            'vehicle_name' : 'Vehicle Name',
            'rc_book_number' : 'Rc No' ,
            'reg_no':'Register No',
            'capacity' : 'Capacity',
            'insurance_from' : 'Insurance Form',
            'insurance_to' : 'Insurance To',
            'insurance_company_name' : 'Company Name',
            'owner_name' : 'Owner Name',
        }

class Complainform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Complainform, self).__init__(*args, **kwargs)
        self.fields['user_master'].choices = [(obj.user_master_id, obj.user_name) for obj in UserMasterTable.objects.all()]
    class Meta:
        model=ComplainMaster
        fields="__all__"
        fields= [ 'user_master','com_description']
        labels = {
            'user_master' : 'User Id',
            'com_description' : 'Description',
        }

class Complainstatusform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Complainstatusform, self).__init__(*args, **kwargs)
        self.fields['com'].choices = [(obj.com_id,obj.com_description) for obj in ComplainMaster.objects.all()]
    class Meta:
        model=ComplainStatus
        fields="__all__"
        fields= ['com', 'com_status_id','com_status_date','com_status']
        labels = {
            'com': 'Complain Id',
            'com_status_id' : 'Status Id',
            'com_status_date' : 'Date',
            'com_status' : 'Status',
        }

class Reviewstatusform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Reviewstatusform, self).__init__(*args, **kwargs)
        self.fields['review'].choices = [(obj.review_id, obj.review_description) for obj in ReviewFeedback.objects.all()]
        self.fields['user'].choices = [(obj.user_master_id, obj.user_name) for obj in UserMasterTable.objects.all()]
    class Meta:
        model=ReviewFeedbackStatus
        fields="__all__"
        fields= ['review_status_id', 'review','status','user']
        labels = {
            'review_status_id': 'Review Status Id',
            'review' : 'Review Id',
            'status' : 'Status',
            'user' : 'User Id',
        }

class Docdetform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Docdetform, self).__init__(*args, **kwargs)
        self.fields['doc'].choices = [(obj.doc_id, obj.doc_number) for obj in DocMaster.objects.all()]
        self.fields['vehc_rout'].choices = [(obj.veh_rout_id, obj.vehc_rout_det) for obj in VehicleRoutMaster.objects.all()]
        self.fields['veh_rout_det'].choices = [(obj.veh_rout_det_id, obj.decription) for obj in VehRoutDetalis.objects.all()]
    class Meta:
        model=DocDetail
        fields="__all__"
        fields= ['doc_detail_id', 'doc','doc_address','vehc_rout','doc_weight','veh_rout_det','total_amount']
        labels = {
            'doc_detail_id': 'Doc Detail Id',
            'doc' : 'Doc Id',
            'doc_address' : 'Doc Address' ,
            'vehc_rout':'Vehicle Rout Id',
            'doc_weight' : 'Doc Weight',
            'veh_rout_det' : 'Vehicle Rout Det Id',
            'total_amount' : 'Total Amount',
        }

class Docform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Docform, self).__init__(*args, **kwargs)
        self.fields['gst_charges'].choices = [(obj.gst_char_id, obj.cgst_per) for obj in Gstcharges.objects.all()]
    class Meta:
        model=DocMaster
        fields="__all__"
        fields= ['doc_id', 'doc_number','doc_date','lr_number','gst_charges','net_amount','is_cancel']
        labels = {
            'doc_id': 'Doc Id',
            'doc_number' : 'Doc Number',
            'doc_date' : 'Doc Date' ,
            'lr_number':'LR Number',
            'gst_charges' : 'GST Charges',
            'net_amount' : 'Net Amount',
            'is_cancel' : 'Is Cancel',
        }

class docvehdetform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(docvehdetform, self).__init__(*args, **kwargs)
        self.fields['doc'].choices = [(obj.doc_id, obj.doc_number) for obj in DocMaster.objects.all()]
        self.fields['veh'].choices = [(obj.vehicle_id, obj.vehicle_name) for obj in VehicleMaster.objects.all()]
        self.fields['vehc_rout'].choices = [(obj.veh_rout_id, obj.vehc_rout_det) for obj in VehicleRoutMaster.objects.all()]
    class Meta:
        model=DocVehDetailsTable
        fields="__all__"
        fields= ['doc_veh_det_id', 'doc','veh','vehc_rout','description']
        labels = {
            'doc_veh_det_id': 'Doc Vehicle Det Id',
            'doc' : 'Doc Id',
            'veh' : 'Vehicle Id',
            'vehc_rout' : 'Vehicle Rout Id',
            'description' : 'Description',
        }

class userdetform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(userdetform, self).__init__(*args, **kwargs)
        self.fields['user_master'].choices = [(obj.user_master_id, obj.user_name) for obj in UserMasterTable.objects.all()]
        # self.fields["user_type"].choices =[(obj.name , obj.value) for obj in UserDetails.USER_TYPES]
    class Meta:
        model=UserDetails
        fields="__all__"
        fields= ['user_deatil_id', 'user_master','user_type','profile_pic','contact','gender','address']
        labels = {
            'user_deatil_id': 'User Detail Id',
            'user_master' : 'User Id',
            'user_type' : 'User Type',
            'profile_pic' : 'Profile Pic',
            'contact' : 'Contact',
            'gender' : 'Gender',
            'address' : 'Address',
        }

class vehroutdetform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(vehroutdetform, self).__init__(*args, **kwargs)
        self.fields['veh_rout'].choices = [(obj.veh_rout_id, obj.vehc_rout_det) for obj in VehicleRoutMaster.objects.all()]
        self.fields['ditrict'].choices = [(obj.district_id, obj.district_name) for obj in DistrictMaster.objects.all()]
        self.fields['state'].choices = [(obj.state_id, obj.stat_name) for obj in StateMasterTable.objects.all()]
        self.fields['city_village'].choices = [(obj.city_village_id, obj.city_village_name) for obj in CityVillageMaster.objects.all()]
    class Meta:
        model=VehRoutDetalis
        fields="__all__"
        fields= ['veh_rout_det_id', 'veh_rout','state','ditrict','city_village','decription','char_bel_50','char_bel_150','char_abo_150']
        labels = {
            'veh_rout_det_id': 'Veh Rout Det Id',
            'veh_rout' : 'Veh Rout Id',
            'state' : 'State Id',
            'ditrict' : 'District Id',
            'city_village' : 'City Id',
            'decription' : 'Description',
            'char_bel_50' : 'Charges Below 50kg',
            'char_bel_150' : 'Charges Below 100kg',
            'char_abo_150' : 'Charges Above 150kg',
        }

class vehroutmasterform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(vehroutmasterform, self).__init__(*args, **kwargs)
        self.fields['from_state'].choices = [(obj.state_id, obj.stat_name) for obj in StateMasterTable.objects.all()]
        self.fields['to_state'].choices = [(obj.state_id, obj.stat_name) for obj in StateMasterTable.objects.all()]
        self.fields['dist'].choices = [(obj.district_id, obj.district_name) for obj in DistrictMaster.objects.all()]
    class Meta:
        model=VehicleRoutMaster
        fields="__all__"
        fields= ['veh_rout_id', 'from_state','to_state','vehc_rout_det','dist']
        labels = {
            'veh_rout_id': 'Veh Rout Id',
            'from_state' : 'From State Id',
            'to_state' : ' To State Id',
            'vehc_rout_det' : 'Veh Rout Det',
            'dist' : 'district_name',
        }

class empcomplainform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(empcomplainform, self).__init__(*args, **kwargs)
    class Meta:
        model=ComplainStatus
        fields="__all__"
        fields= ['com_status']
        labels = {
            'com_status' : 'Complain Status'
        }

class myorderform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(myorderform, self).__init__(*args, **kwargs)
        self.fields['gst_charges'].choices = [(obj.gst_char_id, obj.cgst_per) for obj in Gstcharges.objects.all()]
        self.fields['veh'].choices = [(obj.vehicle_id, obj.vehicle_name) for obj in VehicleMaster.objects.all()]
        self.fields['vehc_rout'].choices = [(obj.from_state, obj.from_state.stat_name+'-'+obj.to_state.stat_name) for obj in VehicleRoutMaster.objects.all()]
        self.fields['dist'].choices = [(obj.district_id, obj.district_name) for obj in DistrictMaster.objects.all()]
        self.fields['veh_rout_det'].choices = [(obj.veh_rout_det_id, obj.decription) for obj in VehRoutDetalis.objects.all()]
    class Meta:
        model=myorderform1
        fields="__all__"
        fields= ['doc_id', 'doc_number','doc_date','lr_number','gst_charges','net_amount','veh','vehc_rout','dist','veh_rout_det']
        labels = {
            'doc_id': 'Doc Id',
            'doc_number' : 'Doc Number',
            'doc_date' : 'Doc Date' ,
            'lr_number':'LR Number',
            'gst_charges' : 'GST Charges',
            'net_amount' : 'Net Amount',
            'veh' : 'Vehicle Name',
            'vehc_rout' : 'To State',
            'dist' : 'District Name',
            'veh_rout_det' : 'Rout Description',
        }