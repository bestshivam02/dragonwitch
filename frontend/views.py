import json
import random
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from numpy import empty
from Products.models import *
from accounts.models import UserAddress
from frontend.models import CategoryBanner, ContactInfo, ContactUs, CountdownBanner, CustomeShirtBanner, HomeFaq, MainCarousel, SaleBanner, Testimonials
from django.contrib import messages
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    username = None

    if request.user.is_authenticated:
        username =  request.user.full_name
    product_all = Product.objects.all().order_by("-id")
    all_categories =  Category.objects.all().order_by("-id")
    product_list = []
    for each in product_all:
        rating_star_obj  = ProductRating.objects.filter(product = each).first()
        rating_star = 0
        if rating_star_obj:
            rating_star = rating_star_obj.rating_star
        wish_list = False
        if request.user.is_authenticated: 
            user_wishlist = UserWishList.objects.filter(product = each , user = request.user )
            if user_wishlist :
                wish_list = True
        product_list.append({
            'id':each.id,
            'name':each.name,
            'price':each.price,
            'discount_price':each.discount_price,
            'description':each.description,
            'image':each.image,
            'rating_star':rating_star,
            'zero_rating_star':(5-rating_star),
            'wish_list':wish_list
        })

    main_carousel =  MainCarousel.objects.filter(is_active=True)
    sale_banner =  SaleBanner.objects.filter(is_active=True)
    sale_counter =  CountdownBanner.objects.filter(is_active=True)
    category_banner =  CategoryBanner.objects.filter(is_active=True)
    custome_shirt_banner =  CustomeShirtBanner.objects.filter(is_active=True)

    context = {
        'username' : username,
        'products' : product_list,
        'main_carousel' : main_carousel,
        'sale_banner' : sale_banner,
        'sale_counter' : sale_counter,
        'category_banner' : category_banner,
        'custome_shirt_banner' : custome_shirt_banner,
        'all_categories' : all_categories,
    }
    if request.user.is_authenticated:
        try:
            token=Token.objects.get(user=request.user)                                        
        except:
            token= Token.objects.create(user=request.user)
        context['token'] = token

    # testing code

    # session_id = request.GET.get('session_id')
    # if session_id is None:
    #     return HttpResponseNotFound()

    # stripe.api_key = settings.STRIPE_SECRET_KEY
    # session = stripe.checkout.Session.retrieve(session_id)
    # raise
    # # order = get_object_or_404(OrderDetail, stripe_payment_intent=session.payment_intent)
    # # order.has_paid = True
    # # order.save()
    # return render(request, 'success.html',context)

    return render(request, 'home.html',context)

"""
User Profile
"""
def profile(request):
    context = {}
    if request.user.is_authenticated:
        order_history = UserOrder.objects.filter(user = request.user)
        user_address = UserAddress.objects.filter(user = request.user)
        context['order_history'] = order_history
        context['user_address'] = user_address
        return render(request, 'frontend/profile.html',context)
    else:
        return redirect('frontend:index')




"""
add product to wish list
"""
def add_product_wishlist(request):
    product = Product.objects.get(id = request.GET.get("id"))
    if not request.user.is_authenticated:
        messages.error(request, 'Please login first ')
        return redirect('frontend:each_products' , product.id )
    user_wishlist = UserWishList.objects.filter( user = request.user )
    
    if UserWishList.objects.filter( user = request.user , product = product ):
        messages.error(request, 'This Product is already added to your wishlist')
        return redirect('frontend:each_products' , product.id )

    wish = UserWishList.objects.create(user = request.user , product =  product)
    if wish:
        messages.success(request, 'Product added to your wishlist')
    else:
        messages.error(request, 'Error while adding to wishlist')
    return render(request, 'frontend/wishlist.html',{"user_wishlist":user_wishlist})

"""
Update User Profile
"""
def updateprofile(request):
    context = {}
    if request.user.is_authenticated:
        # order_history = UserOrderHistory.objects.filter(user = request.user)

        # context['order_history'] = order_history
        if request.method=="POST":
            user_obj = User.objects.filter(id = request.user.id).first()

            if User.objects.filter(email=request.POST.get('user_mail', None)):
                messages.error(request, 'User email is already exists.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if User.objects.filter(mobile_no=request.POST.get('user_phone', None)):
                messages.error(request, 'User Phone No is already exists.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if request.POST.get('user_fname'):
                user_obj.first_name = request.POST.get('user_fname')
            
            if request.POST.get('user_lname'):
                user_obj.last_name = request.POST.get('user_lname')
            
            if request.POST.get('user_fname') and request.POST.get('user_lname'):
                user_obj.full_name = request.POST.get('user_fname') + ' ' + request.POST.get('user_lname')
            
            if request.POST.get('user_fname') and request.POST.get('user_lname'):
                user_obj.full_name = request.POST.get('user_fname') + request.POST.get('user_lname')
            
            if request.POST.get('user_phone'):
                user_obj.mobile_no = request.POST.get('user_phone')
            
            if request.FILES.get('profile_pic'):
                user_obj.profile_pic = request.FILES.get('profile_pic')
            
            if request.POST.get('user_mail'):
                user_obj.email = request.POST.get('user_mail')

            user_obj.save()
            return redirect('frontend:profile')
    else:
        return redirect('frontend:index')

"""
Home Page Banner
"""
@login_required
def main_carousel(request):

    main_carousel =  MainCarousel.objects.filter(is_active=True)
    sale_banner =  SaleBanner.objects.filter(is_active=True)
    sale_counter =  CountdownBanner.objects.filter(is_active=True)
    category_banner =  CategoryBanner.objects.filter(is_active=True)
    custome_shirt_banner =  CustomeShirtBanner.objects.filter(is_active=True)
    context = {
        'main_carousel' : main_carousel,
        'sale_banner' : sale_banner,
        'countdown_banner' : sale_counter,
        'category_banner' : category_banner,
        'custome_shirt_banner' : custome_shirt_banner,
    }
    return render(request, 'admin/frontend/banner.html',context)


@login_required
def edit_main_carousel_dashboard(request,pk):

    main_carousel = MainCarousel.objects.get(pk=pk)
    if request.method=='POST' and main_carousel:
        if request.POST.get('description'):
            main_carousel.description = request.POST.get('description')

        if request.FILES.get('image'):
            main_carousel.image = request.FILES.get('image')

        if request.POST.get('redirect_link'):
            main_carousel.redirect_link = request.POST.get('redirect_link')
        main_carousel.save()
        return redirect('frontend:main_carousel')
    return render(request, 'admin/frontend/main-carousel-edit.html',{'main_carousel':main_carousel})

@login_required
def edit_sale_banner_dashboard(request,pk):

    sale_banner = SaleBanner.objects.get(pk=pk)
    if request.method=='POST' and sale_banner:
        if request.POST.get('description'):
            sale_banner.description = request.POST.get('description')

        if request.FILES.get('image'):
            sale_banner.image = request.FILES.get('image')

        if request.POST.get('redirect_link'):
            sale_banner.redirect_link = request.POST.get('redirect_link')
        sale_banner.save()
        return redirect('frontend:main_carousel')
    return render(request, 'admin/frontend/sale-banner-edit.html',{'main_carousel':sale_banner})

@login_required
def edit_countdown_banner_dashboard(request,pk):

    count_down_banner = CountdownBanner.objects.get(pk=pk)
    product_detail = Product.objects.all()
    if request.method=='POST' and count_down_banner:
        if request.POST.get('description'):
            count_down_banner.description = request.POST.get('description')

        if request.FILES.get('image'):
            count_down_banner.image = request.FILES.get('image')

        if request.POST.get('redirect_link'):
            count_down_banner.redirect_link = request.POST.get('redirect_link')

        if request.POST.get('sale_end_date'):
            count_down_banner.sale_end_date = request.POST.get('sale_end_date')

        if request.POST.get('product'):
            product_obj = Product.objects.filter(name = request.POST.get('product', None)).first()
            count_down_banner.product_detail = product_obj
        count_down_banner.save()
        return redirect('frontend:main_carousel')
    return render(request, 'admin/frontend/count-down-banner-edit.html',{'main_carousel':count_down_banner,'product_detail':product_detail})

@login_required
def edit_category_banner_dashboard(request,pk):

    category_banner = CategoryBanner.objects.get(pk=pk)
    if request.method=='POST' and category_banner:
        if request.POST.get('description'):
            category_banner.description = request.POST.get('description')

        if request.FILES.get('image'):
            category_banner.image = request.FILES.get('image')

        if request.POST.get('redirect_link'):
            category_banner.redirect_link = request.POST.get('redirect_link')
        category_banner.save()
        return redirect('frontend:main_carousel')
    return render(request, 'admin/frontend/category-banner-edit.html',{'main_carousel':category_banner})

@login_required
def edit_custom_shirt_banner_dashboard(request,pk):

    custom_shirt_banner = CustomeShirtBanner.objects.get(pk=pk)
    if request.method=='POST' and custom_shirt_banner:
        if request.POST.get('description'):
            custom_shirt_banner.description = request.POST.get('description')

        if request.FILES.get('image'):
            custom_shirt_banner.image = request.FILES.get('image')

        if request.POST.get('redirect_link'):
            custom_shirt_banner.redirect_link = request.POST.get('redirect_link')
        custom_shirt_banner.save()
        return redirect('frontend:main_carousel')

    return render(request, 'admin/frontend/custom-shirt-banner-edit.html',{'main_carousel':custom_shirt_banner})


"""
each product view
"""
def each_products(request,pk):
    all_product = Product.objects.all()
    each_product_obj = Product.objects.get(pk=pk)
    product_rating_obj = ProductRating.objects.filter(product = each_product_obj).first()
    product_rating =  0
    if product_rating_obj:
        product_rating = product_rating_obj.rating_star
    product_review_obj = ProductReview.objects.filter(product = each_product_obj)
    product_image_obj = ProductImages.objects.filter(product = each_product_obj)
    category_obj = Category.objects.filter(productcategory__product = each_product_obj).first()
    review_count = 0
    rating_gte_5 = ProductReview.objects.filter(product = each_product_obj,rating_star__gte = 4,rating_star__lte = 5).count()
    rating_gte_4 = ProductReview.objects.filter(product = each_product_obj,rating_star__gte = 3,rating_star__lte = 4).count()
    rating_gte_3 = ProductReview.objects.filter(product = each_product_obj,rating_star__gte = 2,rating_star__lte = 3).count()
    rating_gte_2 = ProductReview.objects.filter(product = each_product_obj,rating_star__gte = 1,rating_star__lte = 2).count()
    rating_gte_1 = ProductReview.objects.filter(product = each_product_obj,rating_star__gte = 0,rating_star__lte = 1).count()
    if product_review_obj:
        review_count = product_review_obj.count()

    similar_products = ProductCategory.objects.filter(category = category_obj)
    context = {
            'each_product':each_product_obj,
            'rating':product_rating,
            'zero_start':(5-product_rating),
            'review_count':review_count,
            'reviews':product_review_obj,
            'product_image':product_image_obj,
            'category':category_obj,
            'rating_gte_5':rating_gte_5,
            'rating_gte_4':rating_gte_4,
            'rating_gte_3':rating_gte_3,
            'rating_gte_2':rating_gte_2,
            'rating_gte_1':rating_gte_1,
    }
    all_product_list = []
    for each in all_product:
        rating_star_obj = ProductRating.objects.filter(product = each).first()
        rating_star =  0
        if rating_star_obj:
            rating_star = rating_star_obj.rating_star
        wish_list = False
        if request.user.is_authenticated: 
            user_wishlist = UserWishList.objects.filter(product = each , user = request.user )
            if user_wishlist :
                wish_list = True
            try:
                token=Token.objects.get(user=request.user)
            except:
                token= Token.objects.create(user=request.user)
        all_product_list.append({
            'id':each.id,
            'name':each.name,
            'price':each.price,
            'discount_price':each.discount_price,
            'description':each.description,
            'image':each.image,
            'rating_star':rating_star,
            'zero_rating_star':(5-rating_star),
            'wish_list':wish_list
        })
    similar_products_list = []
    for each in similar_products:
        rating_star_obj = ProductRating.objects.filter(product = each.product).first()
        rating_star =  0
        if rating_star_obj:
            rating_star = rating_star_obj.rating_star
        wish_list = False
        if request.user.is_authenticated: 
            user_wishlist = UserWishList.objects.filter(product = each.product , user = request.user )
            if user_wishlist :
                wish_list = True
            try:
                token=Token.objects.get(user=request.user)
            except:
                token= Token.objects.create(user=request.user)
        similar_products_list.append({
            'id':each.product.id,
            'name':each.product.name,
            'price':each.product.price,
            'discount_price':each.product.discount_price,
            'description':each.product.description,
            'image':each.product.image,
            'rating_star':rating_star,
            'zero_rating_star':(5-rating_star),
            'wish_list':wish_list
        })
    context['all_product'] = all_product_list
    context['similar_products'] = similar_products_list

    if request.user.is_authenticated:
        context['token'],created = Token.objects.get_or_create(user = request.user)
    return render(request, 'frontend/singlepdct.html',context)

"""
all product view
"""
def products(request,pk):

    category_obj = Category.objects.filter(id = pk).first()
    product_all = Product.objects.filter(productcategory__category = category_obj)
    product_list = []
    token = None

    for each in product_all:
        rating_star_obj = ProductRating.objects.filter(product = each).first()
        rating_star =  0
        if rating_star_obj:
            rating_star = rating_star_obj.rating_star
        wish_list = False
        if request.user.is_authenticated: 
            user_wishlist = UserWishList.objects.filter(product = each , user = request.user )
            if user_wishlist :
                wish_list = True
            try:
                token=Token.objects.get(user=request.user)
            except:
                token= Token.objects.create(user=request.user)
        product_list.append({
            'id':each.id,
            'name':each.name,
            'price':each.price,
            'discount_price':each.discount_price,
            'description':each.description,
            'image':each.image,
            'rating_star':rating_star,
            'zero_rating_star':(5-rating_star),
            'wish_list':wish_list
        })
    count =  product_all.count()
    
    context = {
            # 'product_list':product_list,
            "category":category_obj,
            "count":count,
            "token":token,
    }

    all_size = Size.objects.all()
    all_design = Design.objects.all()
    all_material = Material.objects.all()
    all_color = Color.objects.all()

    all_size_dict = {}
    for each in all_size:
        product_size = ProductSize.objects.filter(size = each).count()
        all_size_dict[each.name] = product_size

    all_design_dict = {}
    for each in all_design:
        product_design = ProductDesign.objects.filter(design = each).count()
        all_design_dict[each.name] = product_design

    all_material_dict = {}
    for each in all_material:
        product_material = ProductMaterial.objects.filter(material = each).count()
        all_material_dict[each.name] = product_material

    all_color_dict = {}
    for each in all_color:
        product_color = ProductColor.objects.filter(color = each).count()
        all_color_dict[each.name] = product_color

    context ['all_design'] = all_design_dict
    context ['all_color'] = all_color_dict
    context ['all_size'] = all_size_dict
    context ['all_material'] = all_material_dict

    # Paginator
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    context['product_list'] = page_obj
    return render(request, 'frontend/product.html',context)

"""
Acessories view
"""
def acessories(request):

    context={}

    category_obj =  Category.objects.all()
    if category_obj:
        context['category_obj'] = category_obj
    return render(request, 'frontend/acessories.html',context)

def seach_product(request):
    context = {}
    if request.method=='POST':
        product_obj = None
        if request.POST.get('search'):

            product_obj = Product.objects.filter(name__icontains = request.POST.get('search'))
            product_list = []
            token = None
            if product_obj:
                for each in product_obj:
                    rating_star_obj = ProductRating.objects.filter(product = each).first()
                    rating_star =  0
                    if rating_star_obj:
                        rating_star = rating_star_obj.rating_star
                    wish_list = False
                    if request.user.is_authenticated: 
                        user_wishlist = UserWishList.objects.filter(product = each , user = request.user )
                        if user_wishlist :
                            wish_list = True
                        try:
                            token=Token.objects.get(user=request.user)
                        except:
                            token= Token.objects.create(user=request.user)
                    product_list.append({
                        'id':each.id,
                        'name':each.name,
                        'price':each.price,
                        'discount_price':each.discount_price,
                        'description':each.description,
                        'image':each.image,
                        'rating_star':rating_star,
                        'zero_rating_star':(5-rating_star),
                        'wish_list':wish_list
                    })
            else:
                messages.error(request, 'No Product found with this name')

        context = {
            # 'product_list':product_list,
            "token":token
        }
    all_size = Size.objects.all()
    all_material = Material.objects.all()
    all_color = Color.objects.all()
    all_design = Design.objects.all()

    all_size_dict = {}
    for each in all_size:
        product_size = ProductSize.objects.filter(size = each).count()
        all_size_dict[each.name] = product_size

    all_design_dict = {}
    for each in all_design:
        product_design = ProductDesign.objects.filter(design = each).count()
        all_design_dict[each.name] = product_design

    all_material_dict = {}
    for each in all_material:
        product_material = ProductMaterial.objects.filter(material = each).count()
        all_material_dict[each.name] = product_material

    all_color_dict = {}
    for each in all_color:
        product_color = ProductColor.objects.filter(color = each).count()
        all_color_dict[each.name] = product_color

    context ['all_design'] = all_design_dict
    context ['all_color'] = all_color_dict
    context ['all_size'] = all_size_dict
    context ['all_material'] = all_material_dict

    # Paginator
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    context['product_list'] = page_obj
    
    return render(request, 'frontend/product.html',context)

def filter_product(request):
    context = {}
    product_list = []
    object_list = []
    active_filter_list = []
    if request.method=='POST':

        if request.POST.getlist('Design'):
            for each in request.POST.getlist('Design'):
                object_list.append(ProductDesign.objects.filter(design__name = each))
                active_filter_list.append(each)
                context ['design_check'] = request.POST.getlist('Design')
        if request.POST.getlist('Color'):
            for each in request.POST.getlist('Color'):
                object_list.append(ProductColor.objects.filter(color__name = each))
                active_filter_list.append(each)
                context ['color_check'] = request.POST.getlist('Color')

        if request.POST.getlist('Size'):
            for each in request.POST.getlist('Size'):
                object_list.append(ProductSize.objects.filter(size__name = each))
                active_filter_list.append(each)
                context ['size_check'] = request.POST.getlist('Size')
                
        if request.POST.getlist('Material'):
            for each in request.POST.getlist('Material'):
                object_list.append(ProductMaterial.objects.filter(material__name = each))
                active_filter_list.append(each)
                context ['material_check'] = request.POST.getlist('Material')


        product_list_dict = []
        for each in object_list:
            for each1 in each:
                if each1.product not in product_list:
                    product_list.append(each1.product)

        for each in product_list:
                rating_star_obj = ProductRating.objects.filter(product = each).first()
                rating_star =  0
                if rating_star_obj:
                    rating_star = rating_star_obj.rating_star
                wish_list = False
                if request.user.is_authenticated: 
                    user_wishlist = UserWishList.objects.filter(product = each , user = request.user )
                    if user_wishlist :
                        wish_list = True
                    try:
                        token=Token.objects.get(user=request.user)
                    except:
                        token= Token.objects.create(user=request.user)
                product_list_dict.append({
                    'id':each.id,
                    'name':each.name,
                    'price':each.price,
                    'discount_price':each.discount_price,
                    'description':each.description,
                    'image':each.image,
                    'rating_star':rating_star,
                    'zero_rating_star':(5-rating_star),
                    'wish_list':wish_list
                })
        if request.user.is_authenticated: 
            try:
                token=Token.objects.get(user=request.user)
                context['token'] = token
            except:
                token= Token.objects.create(user=request.user)
                context['token'] = token
        # context['product_list'] = product_list_dict
        

    all_size = Size.objects.all()
    all_material = Material.objects.all()
    all_color = Color.objects.all()
    all_design = Design.objects.all()

    all_size_dict = {}
    for each in all_size:
        product_size = ProductSize.objects.filter(size = each).count()
        all_size_dict[each.name] = product_size

    all_design_dict = {}
    for each in all_design:
        product_design = ProductDesign.objects.filter(design = each).count()
        all_design_dict[each.name] = product_design

    all_material_dict = {}
    for each in all_material:
        product_material = ProductMaterial.objects.filter(material = each).count()
        all_material_dict[each.name] = product_material

    all_color_dict = {}
    for each in all_color:
        product_color = ProductColor.objects.filter(color = each).count()
        all_color_dict[each.name] = product_color

    context ['all_design'] = all_design_dict
    context ['all_color'] = all_color_dict
    context ['all_size'] = all_size_dict
    context ['all_material'] = all_material_dict
    context ['active_filter_list'] = active_filter_list

    # Paginator
    paginator = Paginator(product_list_dict, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    context['product_list'] = page_obj
    return render(request, 'frontend/product.html',context)

"""
User wish list
"""
# @login_required
def userwishlist(request):
    context = {}
    if request.user.is_authenticated:
        user_wishlist_obj = UserWishList.objects.filter(user = request.user)
        try:
            token=Token.objects.get(user=request.user)
        except:
            token= Token.objects.create(user=request.user)
        context['token'] = token

        context['user_wishlist'] = user_wishlist_obj
        return render(request, 'frontend/wishlist.html',context)
    else:
        messages.error(request, 'Please login to view your wish list.')
        return redirect('frontend:index')




"""
User cart list
"""
# @login_required
def usercartlist(request):
    context = {}
    if request.user.is_authenticated:
        user_cartlist_obj = UserCart.objects.filter(user = request.user)
        try:
            token=Token.objects.get(user=request.user)
        except:
            token= Token.objects.create(user=request.user)
        context['token'] = token

        context['user_cartlist'] = user_cartlist_obj
    return render(request, 'frontend/cart.html',context)

"""
User Custome Product
"""
# @login_required
def usercustomeproduct(request):
    context = {}
    home_faq =  HomeFaq.objects.all()
    context['faq'] = home_faq
    return render(request, 'frontend/categories.html',context)

"""
User Custome Shirt
"""
# @login_required
def usercustomeshirt(request):
    context = {}
    # home_faq =  HomeFaq.objects.all()
    # context['faq'] = home_faq
    return render(request, 'frontend/customize.html',context)

"""
User Custome Design
"""
@csrf_exempt
def usercustomedesign(request):
    context = {}
    # home_faq =  HomeFaq.objects.all()
    # context['faq'] = home_faq
    
    if request.method=='POST':
        if request.user.is_authenticated:
            if request.POST.get('front') or request.POST.get('back'):
                custom_product_order = UserCustomDesign.objects.create(
                    product_image = request.POST.get('product_image'),
                    front_desing = request.POST.get('front'),
                    back_desing = request.POST.get('back'),
                    qty = request.POST.get('qty'),
                    amount = request.POST.get('amount'),
                    created_by = request.user,
                    slug = 'custom_product' + request.user.username+'{0:06}'.format(random.randint(1,9999)),
                    is_active = True
                )
                return HttpResponse(status=200)
        else:
            return redirect('frontend:index')
    return render(request, 'frontend/color.html',context)

"""
User cart list
"""

def add_wishlist_to_cart(request):
    context = {}
    if request.user.is_authenticated:
        user_wishlist_obj = UserWishList.objects.filter(user = request.user)
        if user_wishlist_obj:
            for each in user_wishlist_obj:
                    size_obj = Size.objects.all().first()
                    # add condition here for availability of products and for size for product
                    # TODO here for availability and quantity
                    try :

                        user_cartlist_new_obj = UserCart.objects.get(
                            product = each.product,
                            user = request.user
                        )
                        user_cartlist_new_obj.qty += 1
                        user_cartlist_new_obj.size = size_obj
                        user_cartlist_new_obj.price = user_cartlist_new_obj.qty * each.product.price
                        user_cartlist_new_obj.save()
                        
                    except:
                        user_cartlist_new_obj1 = UserCart.objects.create(
                        product = each.product,
                        user = request.user,
                        qty = 1,
                        price = each.product.price,
                        size = size_obj
                        )
            user_wishlist_obj.delete()   
            return redirect('frontend:usercartlist')
        else:
            return redirect('frontend:index')
    else:    
        return redirect('frontend:index')


"""
User checkout
"""
# @login_required
def usercheckout(request):
    context = {}

    if request.user.is_authenticated:
        user_cartlist_obj = UserCart.objects.filter(user = request.user)
        user_custom_order_obj = UserCustomDesign.objects.filter(created_by = request.user,is_active = True)
        user_address_obj = UserAddress.objects.filter(user = request.user).first()

        try:
            token=Token.objects.get(user=request.user)
        except:
            token= Token.objects.create(user=request.user)
        context['token'] = token

        context['user_cartlist'] = user_cartlist_obj
        
        context['user_custom_order'] = user_custom_order_obj

        context['user_address'] = user_address_obj

        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        
        return render(request, 'frontend/checkout.html',context)
    else:
        messages.error(request, 'Please login to checkout.')
        return redirect('frontend:index')
 
"""
User order place
"""
def userorderplaced(request):
    context = {}

    if request.method=='GET' and request.user.is_authenticated:
        # user_cart_list = UserCart.objects.filter(user = request.user)
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(UserOrderHistory, stripe_payment_intent=session.payment_intent)
        empty_list = []

        if order:
            user_order_history = UserOrder.objects.filter(order_history=order,user=request.user)
            if user_order_history:
                for each in user_order_history:
                    product_obj =  each.product
                    pro_quantity = product_obj.quantity - each.qty
                    if pro_quantity > 0 :
                        product_obj.quantity = pro_quantity
                    else:
                        product_obj.quantity = 0
                    product_obj.save()
                    empty_list.append({
                        'Product_name' : each.product.name,
                        'Qty' : each.qty,
                        'Transaction_Amount' : each.amount,
                        'User' : each.user.email,
                    })

                    product_category = ProductCategory.objects.filter(product = product_obj).first()
                    if product_category:
                        cat_qty =  product_category.quantity - each.qty
                        if cat_qty > 0 :
                            product_category.quantity = cat_qty
                        else:
                            product_category.quantity = 0 
                        product_category.save()

                    product_design = ProductDesign.objects.filter(product = product_obj).first()
                    if product_design:
                        des_qty =product_design.quantity - each.qty
                        if des_qty > 0 :
                            product_design.quantity = des_qty
                        else:
                            product_design.quantity = 0

                        product_design.save()

                    product_material = ProductMaterial.objects.filter(product = product_obj).first()
                    if product_material:
                        mat_qty = product_material.quantity - each.qty
                        if mat_qty > 0:
                            product_material.quantity = mat_qty
                        else :
                            product_material.quantity = 0

                        product_material.save()
                    product_size = ProductSize.objects.filter(product = product_obj).first()
                    if product_size:
                        siz_qty = product_size.quantity - each.qty
                        if siz_qty:
                            product_size.quantity = siz_qty
                        else:
                            product_size.quantity = 0

                        product_size.save()
                    product_color = ProductColor.objects.filter(product = product_obj).first()
                    if product_color:
                        col_qty = product_color.quantity - each.qty
                        if col_qty> 0 :
                            product_color.quantity = col_qty
                        else:
                            product_color.quantity = 0

                        product_color.save()
            order.has_paid = True 
            order.tranastion_id.status = True
            order.tranastion_id.save()
            order.save()
            user_cart_list_obj = UserCart.objects.filter(user = request.user)
            user_cart_list_obj.delete()
            user_custom_design_obj = UserCustomDesign.objects.filter(created_by = request.user,is_active = True)
            for each in user_custom_design_obj:
                each.is_active = False
                each.save()
            """
            Notify admin of new order
            """
            try:
                subject = f'New Order is placed'
                context = {
                    'list':empty_list
                }

                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail( subject,
                render_to_string('email/product_email.txt',context), 
                email_from, 
                recipient_list)
            except Exception as e:
                print('error in mail in order placement',e)
                pass
    return render(request, 'frontend/placeorder.html',context)


"""
User create checkout session
"""

@csrf_exempt
def create_checkout_session(request):

    domain_url = settings.DOMAIN_URL

    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        if request.user.is_authenticated:
            request_data = json.loads(request.body)
            if request_data['address'] and request_data['city'] and request_data['state'] and request_data['postal']:
                try:
                    user_adress_obj_old = UserAddress.objects.get(
                        user = request.user,
                        address = request_data['address'],
                        city = request_data['city'],
                        state = request_data['state'],
                        zipcode = request_data['postal']
                    )
                except:
                    user_adress_obj_new = UserAddress.objects.create(
                        user = request.user,
                        address = request_data['address'],
                        city = request_data['city'],
                        state = request_data['state'],
                        zipcode = request_data['postal']
                    )
            list = []
            user_cart_list = UserCart.objects.filter(user = request.user)
            price = 0
            for each in user_cart_list:
                if each.qty <= each.product.quantity:
                    price += (each.qty * each.price * 100)

                    list.append({
                        'name': each.product.name,
                        'quantity': each.qty,
                        'currency': 'inr',
                        'amount': each.price * 100,
                    })
                else:
                    messages.error(request, 'Order qty exceed.')
                    raise ValueError ('Order qty exceed.')
                    # return redirect('frontend:usercheckout')

                    # return JsonResponse({
                    #     'message' : 'Order qty exceed.',
                    #     }, safe=False)
            user_custom_order = UserCustomDesign.objects.filter(created_by = request.user,is_active = True)
            price = 0
            for each in user_custom_order:
                    price += (each.qty * each.amount * 100)
                    name = 'none'
                    if each.name:
                        name=each.name
                    list.append({
                        'name': name,
                        'quantity': each.qty,
                        'currency': 'inr',
                        'amount': each.amount * 100,
                    })

                    # return JsonResponse({
                    #     'message' : 'Order qty exceed.',
                    #     }, safe=False)
            if price <= 500:
                price += (500 * 100)
                list.append({
                    'name': 'Shipping Charges',
                    'quantity': 1,
                    'currency': 'inr',
                    'amount': 500 * 100,
                })
            else:
                list.append({
                    'name': 'Shipping Charges',
                    'quantity': 1,
                    'currency': 'inr',
                    'amount': 0,
                })

            checkout_session = stripe.checkout.Session.create(
                # new
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'order_placed?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=list
            )
            # order_detail_obj =  OrderDetail.objects.create(

            # )
            transaction_id = Transaction.objects.create(
                amount = (checkout_session['amount_total']/100),
                    transactio_id = checkout_session['payment_intent'],
                    data = checkout_session,
                    created_by = request.user,
                    status = False
            )
            price_rupee = price /100
            order_history_obj = UserOrderHistory.objects.create(
                    user = request.user,
                    amount = price_rupee,
                    stripe_payment_intent = checkout_session['payment_intent'],
                    # This field can be changed as status
                    has_paid = False,
                    tranastion_id = transaction_id,
                    slug = 'user_order_history' + request.user.username + checkout_session['payment_intent']
                )

            for each in user_cart_list:

                user_order_obj = UserOrder.objects.create(
                    product = each.product,
                    user = request.user,
                    qty =  each.qty,
                    amount = each.price,
                    stripe_payment_intent = checkout_session['payment_intent'],
                    tranastion_id = transaction_id,
                    order_history =order_history_obj,
                    slug = 'user_order'+request.user.username + checkout_session['payment_intent'] + each.product.name
                )

            for each in user_custom_order:
                user_order_obj = UserCustomProductOrder.objects.create(
                    user_design = each,
                    user = request.user,
                    qty =  each.qty,
                    amount = each.amount,
                    stripe_payment_intent = checkout_session['payment_intent'],
                    tranastion_id = transaction_id,
                    order_history =order_history_obj,
                    slug = 'UserCustomProductOrder'+request.user.full_name+'{0:06}'.format(random.randint(1,9999)) + checkout_session['payment_intent']
                )
            return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
        print("error >>>",e)
        return JsonResponse({'error': str(e)})


# payments/views.py
class CancelledView(TemplateView):
    template_name = 'cancelled.html'

# payments/views.py
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY
    endpoint_secret = "whsec_e0585bc84efe040c70b2375b62aaf20b2e2df9d4980ffe2048aa1c99c6d7dd6d"
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here


    return HttpResponse(status=200)

"""
About Page
"""
# @login_required
def about(request):
    context = {}

    user_testimonials_obj = Testimonials.objects.all()
    context['testimonials'] = user_testimonials_obj
        
    admin_team_obj = User.objects.all().exclude(role_id=3)

    context['admin_team_obj'] = admin_team_obj


    return render(request, 'frontend/about.html',context)

"""
Faq's Page
"""
# @login_required
def faq(request):
    context={}
    home_faq =  HomeFaq.objects.all()
    contact_info_obj =  ContactInfo.objects.filter(is_active = True).first()
    context['faq'] = home_faq
    context['contact_info'] = contact_info_obj
    return render(request, 'frontend/faq.html',context)

"""
Contact Us Page
"""
# @login_required
def contact_us(request):
    context = {}

    if request.method=='POST':
    
        if request.POST.get('name'):
            contact_us_obj = ContactUs.objects.create(
                name = request.POST.get('name')
            )
            if contact_us_obj:
                if request.POST.get('subject'):
                    contact_us_obj.subject = request.POST.get('subject')

                if request.POST.get('message'):
                    contact_us_obj.message = request.POST.get('message')

                if request.POST.get('email'):
                    contact_us_obj.email = request.POST.get('email')

                if request.user.is_authenticated:
                    contact_us_obj.created_by = request.user

                contact_us_obj.save()
            return redirect('frontend:index')
    return render(request, 'frontend/contact.html',context)

"""
Coming Soon Page
"""
def coming_soon(request):


    return render(request, 'frontend/coming_soon.html')

"""
View Testimonials
"""
# @login_required
def view_testimonials(request):
    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        user_testimonials_obj = Testimonials.objects.all()
        context['testimonials'] = user_testimonials_obj

    return render(request, 'admin/frontend/testimonials.html',context)

"""
Add Testimonials
"""
@login_required
def add_testimonials(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        if request.method=='POST':

            

            user_testimonials_obj = Testimonials.objects.create(
                created_by = request.user,
                update_by = request.user
            )
            if user_testimonials_obj:
                if request.POST.get('name'):
                    user_testimonials_obj.name = request.POST.get('name')

                if request.POST.get('review'):
                    user_testimonials_obj.review = request.POST.get('review')

                if request.POST.get('rating_star'):
                    user_testimonials_obj.rating_star = request.POST.get('rating_star')

                if request.FILES.get('image'):
                    user_testimonials_obj.image = request.FILES.get('image')

                user_testimonials_obj.save()
                
                return redirect('frontend:view_testimonials')
            return redirect('frontend:view_testimonials')

    return render(request, 'admin/frontend/testimonials-add.html')
"""
Edit Testimonials
"""
@login_required
def edit_testimonials(request,pk):

    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        user_testimonials_obj = Testimonials.objects.get(pk=pk)

        context['testimonial'] = user_testimonials_obj
        if request.method=='POST' and user_testimonials_obj:
            if request.POST.get('name'):
                user_testimonials_obj.name = request.POST.get('name')

            if request.POST.get('review'):
                user_testimonials_obj.review = request.POST.get('review')
            
            if request.POST.get('rating_star'):
                user_testimonials_obj.rating_star = request.POST.get('rating_star')

            if request.FILES.get('image'):
                user_testimonials_obj.image = request.FILES.get('image')
            
            if request.POST.get('name') or request.POST.get('review') or request.FILES.get('image') or request.FILES.get('rating'):
                user_testimonials_obj.update_by = request.user

            user_testimonials_obj.save()
            return redirect('frontend:view_testimonials')

        return render(request, 'admin/frontend/testimonials-edit.html',context)
    else:
        return redirect('frontend:index')

"""
Delete Testimonials
"""
@login_required
def delete_testimonials(request,pk):

    if request.user.is_authenticated and request.user.role_id == 1:
        user_testimonials_obj = Testimonials.objects.get(pk=pk)
        if request.method=='POST' and user_testimonials_obj:
            user_testimonials_obj.delete()
            return redirect('frontend:view_testimonials')
    return redirect('frontend:index')

"""
View Testimonials
"""
# @login_required
def view_faq(request):
    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        home_faq_obj = HomeFaq.objects.all()
        context['homefaq'] = home_faq_obj

        return render(request, 'admin/frontend/faq_all.html',context)
    else:
        return redirect('frontend:index')

"""
Add FAQ
"""
@login_required
def add_faq(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        if request.method=='POST':
            
            if request.POST.get('question') and request.POST.get('answer'):

                home_faq_obj = HomeFaq.objects.create(
                    question = request.POST.get('question'),
                    answer = request.POST.get('answer')
                )
                            
                return redirect('frontend:view_faq')
            return redirect('frontend:view_faq')

        return render(request, 'admin/frontend/faq-add.html')
    else:
        return redirect('frontend:index')

"""
Edit Faq
"""
@login_required
def edit_faq(request,pk):

    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        faq_obj = HomeFaq.objects.get(pk=pk)

        context['faq'] = faq_obj
        if request.method=='POST' and faq_obj:
            if request.POST.get('question'):
                faq_obj.question = request.POST.get('question')

            if request.POST.get('answer'):
                faq_obj.answer = request.POST.get('answer')

            faq_obj.save()
            return redirect('frontend:view_faq')

        return render(request, 'admin/frontend/faq-edit.html',context)
    else:
        return redirect('frontend:index')

"""
Delete Faq
"""
@login_required
def delete_faq(request,pk):

    if request.user.is_authenticated and request.user.role_id == 1:
        home_faq_obj = HomeFaq.objects.get(pk=pk)
        if request.method=='POST' and home_faq_obj:
            home_faq_obj.delete()
            return redirect('frontend:view_faq')
    else:
        return redirect('frontend:index')

"""
View contact_info
"""
# @login_required
def contact_info(request):
    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        contact_info_obj = ContactInfo.objects.all()
        context['contact_info'] = contact_info_obj

        return render(request, 'admin/frontend/contact_info.html',context)
    else:
        return redirect('frontend:index')

"""
Add Contact Info
"""
@login_required
def add_contact_info(request):

    if request.user.is_authenticated and request.user.role_id == 1:
        if request.method=='POST':

            

            if request.POST.get('email') and request.POST.get('mobile_no'):
                user_ContactInfo_obj = ContactInfo.objects.create(
                    email = request.POST.get('email'),
                    mobile_no = request.POST.get('mobile_no')
                )
            if user_ContactInfo_obj:
                if request.POST.get('name'):
                    user_ContactInfo_obj.name = request.POST.get('name')

                if request.FILES.get('image'):
                    user_ContactInfo_obj.image = request.FILES.get('image')

                if request.POST.get('is_active'):
                    user_ContactInfo_obj.is_active = True

                user_ContactInfo_obj.save()
                
                return redirect('frontend:contact_info')
            return redirect('frontend:contact_info')

        return render(request, 'admin/frontend/contact_info-add.html')
    else:
        return redirect('frontend:index')


"""
Edit Contact Info
"""
@login_required
def edit_contact_info(request,pk):

    context = {}
    if request.user.is_authenticated and request.user.role_id == 1:
        user_ContactInfo_obj = ContactInfo.objects.get(pk=pk)

        context['contact_info'] = user_ContactInfo_obj
        if request.method=='POST' and user_ContactInfo_obj:
            if request.POST.get('name'):
                user_ContactInfo_obj.name = request.POST.get('name')
            
            if request.POST.get('email'):
                user_ContactInfo_obj.email = request.POST.get('email')

            if request.POST.get('mobile_no'):
                user_ContactInfo_obj.mobile_no = request.POST.get('mobile_no')

            if request.FILES.get('image'):
                user_ContactInfo_obj.image = request.FILES.get('image')

            if request.POST.get('is_active'):
                user_ContactInfo_obj.is_active = True

            user_ContactInfo_obj.save()
            return redirect('frontend:contact_info')

        return render(request, 'admin/frontend/contact_info-edit.html',context)
    else:
        return redirect('frontend:index')

"""
Delete Contact Info
"""
@login_required
def delete_contact_info(request,pk):

    if request.user.is_authenticated and request.user.role_id == 1:
        user_testimonials_obj = ContactInfo.objects.get(pk=pk)
        if request.method=='POST' and user_testimonials_obj:
            user_testimonials_obj.delete()
            return redirect('frontend:contact_info')
    return redirect('frontend:index')
