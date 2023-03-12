from django.db import models
from django.contrib.auth.models import AbstractUser
# from Products.models import Product
from .constants import *

# Create your models here.

"""
user model
"""
class User(AbstractUser):
    username = models.CharField(max_length=150,null=True,blank=True,unique=True)
    password = models.CharField(max_length=150,null=True,blank=True,unique=True)
    full_name = models.CharField(max_length=150,null=True,blank=True)
    first_name = models.CharField(max_length=150,null=True,blank=True)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField("email address",unique=True,blank=True, null=True)
    mobile_no = models.CharField(max_length=16,validators=[number], null=True, blank=True, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pic/',default='default.png', blank=True, null=True)
    role_id = models.PositiveIntegerField(choices=USER_ROLE, default=3)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    dob = models.CharField(max_length=150,null=True,blank=True)
    verification_code = models.CharField(max_length=25,null=True,blank=True)
    secondary_mobile_no = models.CharField(max_length=16,validators=[number], null=True, blank=True, unique=True)
    otp_verifY = models.BooleanField(default=False)

    class Meta:
        managed = True;
        db_table = 'tbl_user'

    def __str__(self):
        return str(self.username)

"""
user address model
"""
class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=150,null=True,blank=True)
    city =  models.CharField(max_length=150,null=True,blank=True)
    state = models.CharField(max_length=150,null=True,blank=True)
    zipcode = models.CharField(max_length=150,null=True,blank=True)
    country = models.CharField(max_length=150,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True;
        db_table = 'tbl_user_address'

"""
device type model
"""
class Device(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='device')
    device_type = models.PositiveIntegerField(choices=DEVICE_TYPE,null=True,blank=True)
    device_name = models.CharField(max_length=50,null=True,blank=True)
    device_token = models.CharField(max_length=500,null=True,blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_device'

    def __str__(self):
        return str(self.created_by)

class Transaction(models.Model):
    amount = models.CharField(max_length=255,null=True,blank=True)
    transactio_id = models.CharField(max_length=255,null=True,blank=True)
    receipt = models.FileField(max_length=255,null=True,blank=True)
    status = models.BooleanField(default=False,verbose_name='Transaction Status')
    data = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table  = 'tbl_transaction'

        