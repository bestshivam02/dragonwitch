from .views import *
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^change_passord/$', change_password, name='change_password'),
    url(r'^add_new_address/$', add_new_address, name='add_new_address'),
    url(r'^delete_user_address/(?P<pk>\d+)/$', delete_user_address, name='delete_user_address'),
    # admin dashboard
    url(r'^customers/$', customers_dashboard, name='customers_dashboard'),
    url(r'^add_customers/$', add_customers_dashboard, name='add_customers_dashboard'),
    url(r'^edit_customers/(?P<pk>\d+)/$', edit_customers_dashboard, name='edit_customers_dashboard'),
    url(r'^delete_customer_dashboard/(?P<pk>\d+)/$', deletecustomerdashboard, name='delete_customers_dashboard'),
]