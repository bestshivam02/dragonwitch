from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductCategory)
admin.site.register(ProductRating)
admin.site.register(ProductReview)
admin.site.register(ProductImages)
admin.site.register(UserWishList)
admin.site.register(UserCart)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Design)
admin.site.register(Size)
admin.site.register(ProductMaterial)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductDesign)
admin.site.register(UserOrder)
admin.site.register(UserOrderHistory)
admin.site.register(UserCustomDesign)
admin.site.register(UserCustomProductOrder)
admin.site.register(PromoCode)
admin.site.register(UserPromoCode)