from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from .views import *

admin.autodiscover()
app_name = 'Products'

urlpatterns = [

    url(r'^update_product_review/(?P<pk>\d+)/$', update_product_review, name='update_product_review'),
    url(r'^apply_promo/$', apply_promo, name='apply_promo'),
    # admin dashboard
    # product
    url(r'^dashboard/$', productdashboard, name='product_dashboard'),
    url(r'^add_product_dashboard/$', addproductdashboard, name='add_product_dashboard'),
    url(r'^edit_product_dashboard/(?P<pk>\d+)/$', editproductdashboard, name='edit_product_dashboard'),
    url(r'^delete_product_dashboard/(?P<pk>\d+)/$', deleteproductdashboard, name='delete_product_dashboard'),

    #category
    url(r'^category_dashboard/$', category_dashboard, name='category_dashboard'),
    url(r'^add_category_dashboard/$', addcategorydashboard, name='add_category_dashboard'),
    url(r'^edit_category_dashboard/(?P<pk>\d+)/$', editcategorydashboard, name='edit_category_dashboard'),
    url(r'^delete_category_dashboard/(?P<pk>\d+)/$', deletecategorydashboard, name='delete_category_dashboard'),

    #product type
    url(r'^product_type/$', producttypedashboard, name='product_type_dashboard'),
    url(r'^add_product_type/$', add_producttypedashboard, name='add_product_type_dashboard'),
    
    #product type
    url(r'^order_dashoard/$', order_dashoard, name='order_dashoard'),
    url(r'^order_not_delivered/$', order_not_delivered_dashboard, name='order_not_delivered_dashboard'),
    url(r'^order_delivered/$', order_delivered_dashboard, name='order_delivered_dashboard'),
    url(r'^update_order_delivery_status/(?P<pk>\d+)/$', update_order_delivery_status_dashboard, name='update_order_delivery_status_dashboard'),
]