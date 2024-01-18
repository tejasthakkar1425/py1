import datetime
from django.db import models

# Create your models here.

class state_master_table(models.Model):

    state_id= models.IntegerField(default=0)
    stat_name = models.TextField()
    Description=models.CharField(max_length=50,blank=True,null=True)
    created_by_user_id=models.IntegerField(default=0)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    updated_by_user_id=models.IntegerField(default=0,blank=True,null=True)
    updated_date= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.stat_name
    
    class Meta:
        db_table='state_master_table'

class city_village_master_table(models.Model):
    
    city_village_id= models.IntegerField(default=0)
    district_id = models.IntegerField(default=0)
    state_id=models.IntegerField(default=0)
    city_village_name=models.TextField()
    description=models.CharField(max_length=50,blank=True,null=True)
    created_by_user_id=models.IntegerField(default=0)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    updated_by_user_id=models.IntegerField(default=0,blank=True,null=True)
    updated_date= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.city_village_name
    
    class Meta:
        db_table='city_village_master'
        
        
class gstcharges(models.Model):

    gst_char_id = models.IntegerField(default=0)
    year = models.TextField()
    cgst_per = models.FloatField(default=0,null=True)
    sgst_per = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.gst_char_id
    
    class Meta:
        db_table='gstcharges'
        
class district_master_table(models.Model):
    
    district_id = models.IntegerField(default=0)
    district_name=models.TextField()
    state_id=models.IntegerField(default=0)
    description=models.CharField(max_length=50,blank=True,null=True)
    created_by_user_id=models.IntegerField(default=0)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    updated_by_user_id=models.IntegerField(default=0,blank=True,null=True)
    updated_date= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.district_name
    
    class Meta:
        db_table='district_master'

class doc_master_table(models.Model):
    
    doc_id = models.IntegerField(default=0)
    doc_number=models.IntegerField(default=0)
    doc_date=models.DateTimeField(auto_now_add=True,blank=True)
    LR_number=models.IntegerField(default=0)
    gst_charges_id=models.IntegerField(default=0,blank=True,null=True)
    net_amount=models.FloatField(default=0,null=True)
    is_cancel=models.IntegerField(default=0)


    def __str__(self):
        return self.doc_id
    
    class Meta:
        db_table='doc_master'

class vehicle_master_table(models.Model):
    
    vehicle_id = models.IntegerField(default=0)
    vehicle_name=models.TextField()
    RC_book_number=models.TextField()
    Reg_number=models.IntegerField(default=0)
    capacity=models.FloatField(default=0,null=True)
    insurance_from=models.DateTimeField(auto_now_add=True,blank=True)
    insurance_to=models.DateTimeField(auto_now_add=True,blank=True)
    insurance_company_name=models.TextField()
    owner_name=models.TextField()

    def __str__(self):
        return self.vehicle_id
    
    class Meta:
        db_table='vehicle_master'

class vehicle_route_master_table(models.Model):
    
    vehicle_rout_id = models.IntegerField(default=0)
    from_state_id= models.IntegerField(default=0)
    to_state_id=models.IntegerField(default=0)
    veh_rout_det=models.TextField()
    veh_rout_drt_id=models.IntegerField(default=0)

    def __str__(self):
        return self.vehicle_rout_id
    
    class Meta:
        db_table='vehicle_rout_master'

class user_master_table(models.Model):
    
    user_master_id = models.IntegerField(default=0)
    user_email_id=models.TextField()
    user_name=models.TextField()
    user_password=models.TextField()
    def __str__(self):
        return self.user_master_id
    
    class Meta:
        db_table='user_master_master'

class review_feedback_table(models.Model):
    
    review_id = models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    review_image=models.TextField()
    review_decription=models.TextField()
    review_star=models.IntegerField(default=0)
    def __str__(self):
        return self.review_id
    
    class Meta:
        db_table='review&feedback_master'