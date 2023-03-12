import json
import stripe
from .models import *
from django.views import View
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from Products.models import UserOrderHistory
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

"""
User Login
"""
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'registration/login.html')   

    def post(self,request,*args,**kwargs):

        if request.method=='POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            # agent=request.META['HTTP_USER_AGENT']
            IP=request.META.get("REMOTE_ADDR")
            des= request.path
            urls="http://"+IP+des
            if not email:
                messages.error(request, 'Please enter email.')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

            if not password:
                messages.error(request, 'Please type password.')
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

            if request.POST.get('remember_me')=='on':
                request.session.set_expiry(1209600) 

            user = authenticate(username=email, password=password)
            if not user:
                messages.error(request, 'Invalid login details.')
                return redirect('frontend:index')

            if user.is_superuser and user.role_id == 1:
                login(request, user)
                return redirect('admin:index')

            # elif user.is_active == True and user.role_id == 3:
            #     login(request, user)
            #     return redirect('hospital:hospital_dashboard')

            # elif user.is_active == True and user.role_id == 4:
            #     login(request, user)
            #     return redirect('doctor:doctor')

            login(request, user)

            messages.success(request, 'logged in succesfull')
            return redirect ('frontend:index')
        else:
            messages.error(request, 'Email not verified, please activate you account on link sent to your email')
            return redirect('accounts:login')
        # login(request, user)
        # return redirect('frontend:index')

"""
User Registeration
"""
class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'registration/login.html')   

    def post(self,request,*args,**kwargs):

        if request.method=='POST':
            if not request.POST.get('email', None):
                messages.error(request, 'Registration failed! Please enter details.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if not request.POST.get('phone', None):
                messages.error(request, 'Registration failed! Please enter details.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if User.objects.filter(email=request.POST.get('email', None)):
                messages.error(request, 'User already exist with this email id.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if User.objects.filter(mobile_no=request.POST.get('phone', None)):
                messages.error(request, 'User already exist with this mobile no.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user = User.objects.create(
                full_name =request.POST.get('name'),
                email=request.POST.get('email'),
                mobile_no=request.POST.get('phone'),
                username=request.POST.get('email'),
                password=request.POST.get('password'),
            )
            user.set_password(user.password)
            customer = stripe.Customer.create(
                description=f"Denver user - {user.id}",
                email = user.email
            )
            user.stripe_customer_id = customer.id
            # user.is_active = False

            # user.verification_code = '{0:04}'.format(random.randint(1,9999))
            # current_site = get_current_site(request)
            # context = {
            #     'user':user, 'domain':current_site.domain,
            #     'url':'/accounts/activate/',
            # }
            # message = render_to_string('accounts/email/verify_email.html', context)

            # mail_subject = 'Activate your account.'
            # # to_email = user.verification_code
            # to_email = request.POST.get('email', None)
            # print("email",to_email)
            # email_message = EmailMultiAlternatives(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            # html_email = render_to_string('accounts/email/verify_email.html',context)
            # email_message.attach_alternative(html_email, 'text/html')
            # email_message.send()

            # messages.add_message(request, messages.INFO, 'Email sent for verfication, an otp is sent to your email.Please activate you account on link sent to your email please Enter this otp ' + user.verification_code )
            user.save()

            return redirect ('frontend:index')

"""
User logout
"""
class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect ('frontend:index')

    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            pass

@login_required
def customers_dashboard(request):

	all_customers = User.objects.all().exclude(role_id=1)

	return render(request, 'admin/customer/eco-customers.html',{"all_customers":all_customers})

@login_required
def add_customers_dashboard(request):

    if request.method=='POST':

        if User.objects.filter(email=request.POST.get('email', None)):
            messages.error(request, 'User email is already exists.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if User.objects.filter(mobile_no=request.POST.get('mobile_no', None)):
            messages.error(request, 'User Phone No is already exists.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = User.objects.create(
            email = request.POST.get('email')
        )
        if user_obj:
            if request.POST.get('full_name'):
                user_obj.full_name = request.POST.get('full_name')

            if request.POST.get('dob'):
                user_obj.dob = request.POST.get('dob')

            if request.POST.get('role_id'):
                user_obj.role_id = request.POST.get('role_id')

            if request.FILES.get('profile_pic'):
                user_obj.profile_pic = request.FILES.get('profile_pic')

            if request.POST.get('mobile_no'):
                user_obj.mobile_no = request.POST.get('mobile_no')

            user_obj.save()
            if request.POST.get('address'):
                user_address = UserAddress.objects.create(
                    user =  user_obj,
                    address = request.POST.get('address'),
                    city = request.POST.get('city'),
                    state = request.POST.get('state'),
                    zipcode = request.POST.get('zipcode'),
                )

    return render(request, 'admin/customer/eco-customer-add.html')

@login_required
def edit_customers_dashboard(request,pk):

    user_obj = User.objects.get(pk=pk)
    user_address_obj = UserAddress.objects.filter(user = user_obj).first()

    if request.method=='POST' and user_obj:
        if request.POST.get('full_name'):
            user_obj.full_name = request.POST.get('full_name')

        if request.FILES.get('profile_pic'):
            user_obj.profile_pic = request.FILES.get('profile_pic')

        if request.POST.get('dob'):
            user_obj.dob = request.POST.get('dob')

        if request.POST.get('email'):
            user_obj.email = request.POST.get('email')

        if request.POST.get('role_id'):
            user_obj.role_id = request.POST.get('role_id')

        if request.POST.get('mobile_no'):
            user_obj.mobile_no = request.POST.get('mobile_no')

        user_obj.save()
    return render(request, 'admin/customer/eco-customer-edit.html',{"user_obj":user_obj,"user_address_obj":user_address_obj})


@login_required
def deletecustomerdashboard(request,pk):

    user_obj = User.objects.get(pk=pk)
    user_address_obj = UserAddress.objects.filter(user = user_obj).all()
    if request.method=='POST' and user_obj:
        user_obj.delete()
        for each in user_address_obj:
            each.delete()
        return redirect('accounts:customers_dashboard')
    return render(request, 'admin/customer/eco-customer-edit.html',{"user_obj":user_obj,"user_address_obj":user_address_obj})

"""
Change User Password
"""
def change_password(request):

    context = {}
    if request.user.is_authenticated:
        order_history = UserOrderHistory.objects.filter(user = request.user)
        context['order_history'] = order_history
        if request.method=="POST":

            user_obj = User.objects.filter(id = request.user.id).first()

            if request.POST.get('oldpassword') and request.POST.get('newpassword'):
                if user_obj.check_password(request.POST.get('oldpassword')):

                    user_obj.set_password(request.POST.get('newpassword'))
                    user_obj.save()
                else:
                    messages.error(request, 'current password is not matched.')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return redirect('frontend:profile')
    else:
        return redirect('frontend:index')

"""
Add new address
"""
def add_new_address(request):

    context = {}
    if request.user.is_authenticated:
        if request.method=="POST":
            request_data = request.POST

            if request_data['address'] and request_data['city'] and request_data['state'] and request_data['postal'] and request_data['country']:
                try:
                    user_adress_obj_old = UserAddress.objects.get(
                        user = request.user,
                        address = request_data['address'],
                        city = request_data['city'],
                        state = request_data['state'],
                        zipcode = request_data['postal'],
                        country = request_data['country']
                    )
                except:
                    user_adress_obj_new = UserAddress.objects.create(
                        user = request.user,
                        address = request_data['address'],
                        city = request_data['city'],
                        state = request_data['state'],
                        zipcode = request_data['postal'],
                        country = request_data['country']
                    )

        return redirect('frontend:profile')
    else:
        return redirect('frontend:index')

"""
Delete user address
"""
def delete_user_address(request,pk):
    context = {}
    if request.user.is_authenticated:
        user_adress_obj_old = UserAddress.objects.filter(id=pk,user=request.user)

        if user_adress_obj_old:
            user_adress_obj_old.delete()

        return redirect('frontend:profile')
    else:
        return redirect('frontend:index')

