from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import * 
app_name = 'frontend'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^add-product-wishlist', views.add_product_wishlist, name='add_product_wishlist'),
    url(r'^updateprofile', views.updateprofile, name='updateprofile'),
    url(r'^product/(?P<pk>\d+)/$', each_products, name='each_products'),
    url(r'^products/(?P<pk>\d+)/$', products, name='products'),
    url(r'^acessories', acessories, name='acessories'),
    url(r'^filter_product', filter_product, name='filter_product'),
    url(r'^search', seach_product, name='seach_product'),
    url(r'^wishlist', userwishlist, name='userwishlist'),
    url(r'^add_wishlist_to_cart', add_wishlist_to_cart, name='add_wishlist_to_cart'),
    url(r'^cartlist', usercartlist, name='usercartlist'),
    url(r'^customeproduct', usercustomeproduct, name='usercustomeproduct'),
    url(r'^customeshirt', usercustomeshirt, name='usercustomeshirt'),
    url(r'^customedesign', usercustomedesign, name='usercustomedesign'),
    url(r'^checkout', usercheckout, name='usercheckout'),
    url(r'^order_placed', userorderplaced, name='userorderplaced'),
    url(r'^create_checkout_session', create_checkout_session, name='create_checkout_session'),
    url(r'^about', about, name='about'),
    url(r'^faq', faq, name='faq'),
    url(r'^contact_us', contact_us, name='contact_us'),
    url(r'^coming_soon', coming_soon, name='coming_soon'),
    # path('cancelled/', views.CancelledView.as_view()),
    # path('webhook/', views.stripe_webhook), # new

    # admin dashboard
    url(r'^main_carousel', main_carousel, name='main_carousel'),
    url(r'^edit_main_carousel_dashboard/(?P<pk>\d+)/$', edit_main_carousel_dashboard, name='edit_main_carousel_dashboard'),
    url(r'^edit_sale_banner_dashboard/(?P<pk>\d+)/$', edit_sale_banner_dashboard, name='edit_sale_banner_dashboard'),
    url(r'^edit_countdown_banner_dashboard/(?P<pk>\d+)/$', edit_countdown_banner_dashboard, name='edit_countdown_banner_dashboard'),
    url(r'^edit_category_banner_dashboard/(?P<pk>\d+)/$', edit_category_banner_dashboard, name='edit_category_banner_dashboard'),
    url(r'^edit_custom_shirt_banner_dashboard/(?P<pk>\d+)/$', edit_custom_shirt_banner_dashboard, name='edit_custom_shirt_banner_dashboard'),
    url(r'^view_testimonials', view_testimonials, name='view_testimonials'),
    url(r'^add_testimonials', add_testimonials, name='add_testimonials'),
    url(r'^edit_testimonials/(?P<pk>\d+)/$', edit_testimonials, name='edit_testimonials'),
    url(r'^delete_testimonials/(?P<pk>\d+)/$', delete_testimonials, name='delete_testimonials'),
    url(r'^view_faq', view_faq, name='view_faq'),
    url(r'^add_faq', add_faq, name='add_faq'),
    url(r'^edit_faq/(?P<pk>\d+)/$', edit_faq, name='edit_faq'),
    url(r'^delete_faq/(?P<pk>\d+)/$', delete_faq, name='delete_faq'),
    url(r'^contact_info', contact_info, name='contact_info'),
    url(r'^add_contact_info', add_contact_info, name='add_contact_info'),
    url(r'^edit_contact_info/(?P<pk>\d+)/$', edit_contact_info, name='edit_contact_info'),
    url(r'^delete_contact_info/(?P<pk>\d+)/$', delete_contact_info, name='delete_contact_info'),
]