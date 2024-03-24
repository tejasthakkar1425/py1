import datetime
from django.db import models

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CityVillageMaster(models.Model):
    city_village_id = models.IntegerField(primary_key=True)
    district = models.ForeignKey('DistrictMaster', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('StateMasterTable', models.DO_NOTHING, blank=True, null=True)
    city_village_name = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=50)
    created_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='cityvillagemaster_updated_by_user_set', blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_village_master'


class ComplainMaster(models.Model):
    com_id = models.IntegerField(primary_key=True)
    user_master = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    com_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain_master'


class ComplainStatus(models.Model):
    com = models.ForeignKey(ComplainMaster, models.DO_NOTHING)
    com_status_id = models.IntegerField(primary_key=True)
    com_status_date = models.DateField(blank=True, null=True)
    com_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain_status'


class DistrictMaster(models.Model):
    district_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(blank=True, null=True,max_length=20)
    state = models.ForeignKey('StateMasterTable',on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50)
    created_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='districtmaster_updated_by_user_set', blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_master'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DocDetail(models.Model):
    doc_detail_id = models.IntegerField(primary_key=True)
    doc = models.ForeignKey('DocMaster', models.DO_NOTHING,null=True)
    doc_address = models.CharField(max_length=100, blank=True, null=True)
    vehc_rout = models.ForeignKey('VehicleRoutMaster', models.DO_NOTHING,null=True)
    doc_weight = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    veh_rout_det = models.ForeignKey('VehRoutDetalis', models.DO_NOTHING,null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_detail'


class DocMaster(models.Model):
    doc_id = models.IntegerField(primary_key=True)
    doc_number = models.IntegerField(blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    lr_number = models.IntegerField(db_column='LR_number', blank=True, null=True)  # Field name made lowercase.
    gst_charges = models.ForeignKey('Gstcharges', models.DO_NOTHING, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_cancel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_master'


class DocVehDetailsTable(models.Model):
    doc_veh_det_id = models.IntegerField(primary_key=True)
    doc = models.ForeignKey(DocMaster, models.DO_NOTHING,null=True)
    veh = models.ForeignKey('VehicleMaster', models.DO_NOTHING,null=True)
    vehc_rout = models.ForeignKey('VehicleRoutMaster', models.DO_NOTHING,null=True)
    description = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'doc_veh_details_table'


class User(models.Model):
    user_master_id = models.IntegerField(primary_key=True)
    user_email_id = models.TextField()
    user_name = models.TextField()
    user_password = models.TextField()

    def __str__(self):   
        managed = False
        db_table = 'user_master_tabel'



class Gstcharges(models.Model):
    gst_char_id = models.IntegerField(primary_key=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    cgst_per = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sgst_per = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstcharges'


class PaymentMaster(models.Model):
    doc_pay_detail = models.TextField(blank=True)
    doc_pay_detail_id = models.IntegerField(primary_key=True)
    doc = models.ForeignKey(DocMaster, models.DO_NOTHING,null=True)
    pay_status = models.TextField(blank=True, null=True)
    pay_method = models.TextField(blank=True, null=True)
    pay_tran_id = models.IntegerField(blank=True, null=True)
    pay_response = models.TextField()

    class Meta:
        managed = False
        db_table = 'payment_master'


class ReviewFeedback(models.Model):
    review_id = models.IntegerField(db_column='Review_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    review_image = models.CharField(db_column='Review_image', max_length=10)  # Field name made lowercase.
    review_description = models.TextField(db_column='Review_description')  # Field name made lowercase.
    review_star = models.IntegerField(db_column='Review_star')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review&feedback'


class ReviewFeedbackStatus(models.Model):
    review_status_id = models.IntegerField(db_column='Review_status_id', primary_key=True)  # Field name made lowercase.
    review = models.ForeignKey(ReviewFeedback, models.DO_NOTHING, db_column='Review_id',null=True)  # Field name made lowercase.
    status = models.TextField(blank=True, null=True)
    user = models.ForeignKey('UserMasterTable', models.DO_NOTHING,null=True)
    created_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='reviewfeedbackstatus_created_by_user_set', blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='reviewfeedbackstatus_updated_by_user_set', blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review&feedback_status'


class StateMasterTable(models.Model):
    state_id = models.IntegerField(primary_key=True)
    stat_name = models.TextField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    created_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    updated_by_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, related_name='statemastertable_updated_by_user_set', blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_master_table'


class UserDetails(models.Model):
    user_deatil_id = models.IntegerField(primary_key=True)
    user_master = models.ForeignKey('UserMasterTable', models.DO_NOTHING,null=True)
    user_type = models.IntegerField(blank=True, null=True)
    profile_pic = models.TextField()
    contact = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_details'


class UserMasterTable(models.Model):
    user_master_id = models.IntegerField(primary_key=True)
    user_email_id = models.TextField()
    user_name = models.TextField()
    user_password = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_master_table'

class VehRoutDetalis(models.Model):
    veh_rout_det_id = models.IntegerField(primary_key=True)
    veh_rout = models.ForeignKey('VehicleRoutMaster', models.DO_NOTHING,null=True)
    state = models.ForeignKey(StateMasterTable, models.DO_NOTHING,null=True)
    ditrict = models.ForeignKey(DistrictMaster, models.DO_NOTHING,null=True)
    city_village = models.ForeignKey(CityVillageMaster, models.DO_NOTHING,null=True)
    decription = models.TextField()
    char_bel_50 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    char_bel_150 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    char_abo_150 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veh_rout_detalis'


class VehicleMaster(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_name = models.TextField()
    rc_book_number = models.CharField(db_column='RC_book_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reg_no = models.IntegerField(db_column='Reg_no', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(blank=True, null=True)
    insurance_from = models.DateTimeField(blank=True, null=True)
    insurance_to = models.DateTimeField(blank=True, null=True)
    insurance_company_name = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_master'


class VehicleRoutMaster(models.Model):
    veh_rout_id = models.IntegerField(primary_key=True)
    from_state = models.ForeignKey(StateMasterTable, models.DO_NOTHING, blank=True, null=True)
    to_state = models.ForeignKey(StateMasterTable, models.DO_NOTHING, related_name='vehicleroutmaster_to_state_set', blank=True, null=True)   
    vehc_rout_det = models.TextField(blank=True, null=True)
    veh_rout_details = models.ForeignKey(VehRoutDetalis, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_rout_master'