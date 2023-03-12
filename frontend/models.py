from django.db import models
from Products.models import Product
from accounts.models import User
from accounts.constants import number
# Create your models here.

"""
Main carousel banner
"""
class MainCarousel(models.Model):
    image = models.ImageField(upload_to='main_carousel/', blank=True, null=True)
    description = models.CharField(max_length=650,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    redirect_link = models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        managed = True;
        db_table = 'tbl_main_carousel'

"""
sale banner
"""
class SaleBanner(models.Model):
    image = models.ImageField(upload_to='sale_banner/', blank=True, null=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    discounts = models.CharField(max_length=250,null=True,blank=True)
    redirect_link = models.CharField(max_length=250,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True;
        db_table = 'tbl_sale_banner'

"""
countdown banner
"""
class CountdownBanner(models.Model):
    image = models.ImageField(upload_to='countdown_banner/', blank=True, null=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    product_detail = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_end_date = models.DateTimeField(null=True,blank=True)
    redirect_link = models.CharField(max_length=250,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True;
        db_table = 'tbl_countdown_banner'

"""
category banner
"""
class CategoryBanner(models.Model):
    image = models.ImageField(upload_to='countdown_banner/', blank=True, null=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    redirect_link = models.CharField(max_length=250,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True;
        db_table = 'tbl_category_banner'

"""
custome shirt banner
"""
class CustomeShirtBanner(models.Model):
    image = models.ImageField(upload_to='countdown_banner/', blank=True, null=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    redirect_link = models.CharField(max_length=250,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True;
        db_table = 'tbl_custom_shirt_banner'


"""
user comments
"""
class Testimonials(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    review = models.TextField()
    image = models.ImageField(upload_to='testimonials_img/', blank=True, null=True)
    rating_star = models.FloatField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created')
    update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='update')

    class Meta:
        managed = True
        db_table  = 'tbl_testimonials'

"""
FAQ
"""
class HomeFaq(models.Model):
    question = models.CharField(max_length=300,null=True,blank=True)
    answer = models.CharField(max_length=300,null=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_home_faq'

"""
Contact Us
"""
class ContactUs(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=300,null=True,blank=True)
    message = models.TextField()
    email = models.EmailField("email address",blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_contact_us',null=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_contact_us'

"""
Our Contact Info
"""
class ContactInfo(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    email = models.EmailField("email address",blank=True, null=True)
    image = models.ImageField(upload_to='our_contact_info_img/', blank=True, null=True)
    mobile_no = models.CharField(max_length=16,validators=[number], null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table  = 'tbl_our_contact_info'
