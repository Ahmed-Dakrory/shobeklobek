from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

# Create your models here.
class account_type(models.Model):
    type_number = models.IntegerField(default=0)
    type_name =  models.CharField(max_length=50)
    type_description = models.CharField(max_length=1024,default=None)
    type_description_mini = models.CharField(max_length=1024,default=None)
    type_img = models.ImageField(upload_to='imgs/helpers/')
    type_img_mini = models.ImageField(upload_to='imgs/helpers/',default='/img/helpers/broker-01.png')
    allow_post = models.BooleanField(default=False)
    allow_buy = models.BooleanField(default=False)

    class Meta:
        db_table = "account_type"

    def __str__(self):
        return self.type_name


class account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500,default=None)
    phone = models.CharField(max_length=500,default=None)
    user_country = models.CharField(max_length=15,default=None)
    user_city = models.CharField(max_length=15,default=None)
    user_zip = models.CharField(max_length=15,default=None)
    accountType = models.ForeignKey(account_type, on_delete=models.CASCADE)


    company_name = models.CharField(max_length=500,default=None)
    company_hours_of_operation = models.CharField(max_length=500,default=None)
    company_Latitude = models.FloatField(max_length=50,default=None)
    company_Longitude = models.FloatField(max_length=50,default=None)
    company_url = models.CharField(max_length=500,default=None)
    company_description = models.CharField(max_length=500,default=None)
    
   
    class Meta:
        db_table = "account"


    def to_json(self):
        return {
            'id' :self.id,
            'company_name' :self.company_name,
            'company_address' :self.company_address,
            'accountType__type_name' :self.accountType.type_name,
            'user__is_active' :self.user.is_active,
            'user__username' :self.user.username
        } 

    def __str__(self):
        return self.user.username


