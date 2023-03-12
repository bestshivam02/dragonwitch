from .views import *
from django.conf.urls import url
from django.urls import include, path



urlpatterns = [
    url(r'filter_product/$',filter_product.as_view(),name="filter_product"),
    url(r'add_user_wishlist/$',Add_user_wish_list_item.as_view(),name="Add_user_wish_list_item"),
    url(r'delete_user_wishlist/$',delete_user_wish_list_item.as_view(),name="delete_user_wish_list_item"),
    url(r'add_user_cartlist/$',Add_user_cart_list_item.as_view(),name="Add_user_cart_list_item"),
    url(r'delete_user_cartlist/$',delete_user_cart_list_item.as_view(),name="delete_user_cart_list_item"),
]