from Products.models import Category, UserWishList, UserCart
from frontend.models import ContactInfo
from frontend.views import usercartlist

def all_category(request):
    all_category_obj = Category.objects.all()
    our_contact_info_obj = ContactInfo.objects.filter(is_active = True).first()
    user_wishlist_count = 0
    user_cart_count = 0
    if request.user.is_authenticated: 
        username =  request.user.full_name
        user_wishlist_count =  UserWishList.objects.filter(user =  request.user).count()
        user_cart_count =  UserCart.objects.filter(user =  request.user).count()
        user_cart_count =  UserCart.objects.filter(user =  request.user).count()
    return{
        'all_category':all_category_obj,
        'user_wishlist_count' : user_wishlist_count,
        'our_contact_info' : our_contact_info_obj,
        'user_cart_count' : user_cart_count,
    }