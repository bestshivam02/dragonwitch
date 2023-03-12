from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Device)
admin.site.register(UserAddress)
# admin.site.register(UserPurchase)
admin.site.register(Transaction)