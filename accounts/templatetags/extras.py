import datetime as dt
from datetime import datetime ,timezone
from django import template
from accounts.models import *
from django.contrib.auth import get_user_model
from Products.models import * 
from sys import exc_info

User = get_user_model()
register = template.Library()

@register.filter(name='all_userlist')
def all_userlist(key):
	return User.objects.all().exclude(role_id=1)