from django.db import models
from django.forms import SlugField
from django.shortcuts import reverse
from accounts.models import User,Transaction
from accounts.constants import *
# Create your models here.

"""
Category
"""
class Category(models.Model):
    name = models.CharField(max_length=75, unique=True,blank=True)
    image = models.ImageField(upload_to='category_img/',default='category_default.png',)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_category'

    def get_absolute_url(self):
        return reverse('product_by_category', args=(self.slug,))

"""
Product
"""
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveBigIntegerField()
    discount_price = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_img/')
    size = models.PositiveIntegerField(choices=SIZE, default=2)
    quantity = models.PositiveIntegerField(default=1)
    create_on =  models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        managed = True
        db_table  = 'tbl_product'

    def __str__(self):
        return self.name

    def set_discount(self, percentage):
        self.discount_price = self.price * (1 - percentage)
        self.save()

    @property
    def is_discounted(self):
        return bool(self.discount_price)

    def remove_discount(self):
        self.discount_price = None
        self.save()

"""
MATERIAL
"""
class Material(models.Model):
    name = models.CharField(max_length=75, unique=True,blank=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_material'

"""
Product relation with Material
"""
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_material'

"""
SIZE
"""
class Size(models.Model):
    name = models.CharField(max_length=75, unique=True,blank=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)
    class Meta:
        managed = True
        db_table  = 'tbl_size'

"""
Product relation with Size
"""
class ProductSize(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_size'

"""
COLOR
"""
class Color(models.Model):
    name = models.CharField(max_length=75, unique=True,blank=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_color'

"""
Product relation with Color
"""
class ProductColor(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_color'

"""
DESIGN
"""
class Design(models.Model):
    name = models.CharField(max_length=75, unique=True,blank=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_desgin'

"""
Product relation with Design
"""
class ProductDesign(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    design = models.ForeignKey(Design,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_design'

"""
Product relation with Category
"""
class ProductCategory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_category'

"""
Product Image
"""
class ProductImages(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='product_img/',verbose_name='product_image',null=True,blank=True)

"""
Product Rating
"""
class ProductRating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_rating')
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating_star = models.FloatField(null=True,blank=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_rating'

"""
User Product Rating
"""
# class UserProductRating(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_rating')
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     rating_star = models.FloatField(null=True,blank=True)
#     class Meta:
#         managed = True
#         db_table  = 'tbl_product_rating'

"""
Product Review
"""
class ProductReview(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.ForeignKey(ProductRating,on_delete=models.CASCADE,blank=True,null=True)
    rating_star = models.FloatField(null=True,blank=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    review = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table  = 'tbl_product_review'

"""
User Cart
"""
class UserCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty =  models.IntegerField()
    price = models.PositiveBigIntegerField()
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table  = 'tbl_user_cart'

"""
User WishList
"""
class UserWishList(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table  = 'tbl_user_wishlist'

"""
User Order History
"""
class UserOrderHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Amount')

    stripe_payment_intent = models.CharField(max_length=200)

    # This field can be changed as status
    has_paid = models.BooleanField(default=False,verbose_name='Payment Status')
    tranastion_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)
    has_delivered = models.BooleanField(default=False,verbose_name='Delivery Status')
    class Meta:
        managed = True
        db_table  = 'tbl_user_order_history'

"""
User Order
"""
class UserOrder(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty =  models.IntegerField()
    amount = models.IntegerField(verbose_name='Amount')

    stripe_payment_intent = models.CharField(max_length=200)

    # This field can be changed as status
    tranastion_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    order_history = models.ForeignKey(UserOrderHistory,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_user_order'

"""
User Custom design
"""
class UserCustomDesign(models.Model):
    name = models.CharField(max_length=75, null=True,blank=True)
    qty =  models.IntegerField()
    amount = models.IntegerField(verbose_name='customAmount')
    product_image = models.TextField(null=True,blank=True)
    front_desing = models.TextField(null=True,blank=True)
    back_desing = models.TextField(null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        managed = True
        db_table  = 'tbl_user_custom_design'


"""
User Custom Porudct Order
"""
class UserCustomProductOrder(models.Model):
    user_design = models.ForeignKey(UserCustomDesign,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty =  models.IntegerField()
    amount = models.IntegerField(verbose_name='Amount')

    stripe_payment_intent = models.CharField(max_length=200)

    # This field can be changed as status
    tranastion_id = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    order_history = models.ForeignKey(UserOrderHistory,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_user_custom_product_order'

"""
Promo Code
"""
class PromoCode(models.Model):
    name=models.CharField(max_length=75)
    is_active = models.BooleanField(default=True)
    percentage = models.PositiveBigIntegerField(verbose_name='percentage')
    slug = models.SlugField(max_length=75, unique=True,blank=True)

    class Meta:
        managed = True
        db_table  = 'tbl_promo_code'

"""
User Promo Code
"""
class UserPromoCode(models.Model):
    promocode = models.ForeignKey(PromoCode,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table  = 'tbl_user_promo_code'