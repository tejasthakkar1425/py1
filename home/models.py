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
