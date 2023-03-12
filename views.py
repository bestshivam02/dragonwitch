import imp
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import views,status,permissions
import sys
import json
from Products.models import Product, ProductDesign, Size, UserCart, UserWishList
# Create your views here.

"""
Add User wish list item
"""
class Add_user_wish_list_item(views.APIView): 
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        try:
            if request.GET.get('product_name') and request.GET.get('product_id'):
                product_id = int(request.GET.get('product_id').replace('wishlist',''))
                products_obj = Product.objects.filter(id= product_id).first()
                if products_obj:
                    try :
                        user_wishlist_new_obj = UserWishList.objects.get(
                            product = products_obj,
                            user = request.user
                        )
                    except:
                        user_wishlist_new_obj = UserWishList.objects.create(
                        product = products_obj,
                        user = request.user
                    )
                response = {
                'message':'Succesfully added',
                'data':"data",
                'status' : 200,  
                'url' : request.path,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                print("Product id is not valid")
                response = {
                    'message':'id is not found',
                    'data':"data",
                    'status' : 400,
                    'url' : request.path,
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            print("delete user wish list",sys.exc_info())
            response = {
                    'message':'Something went wrong.',
                    'data':"data",
                    'status' : 500,
                    'url' : request.path,
            }
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Delete User wish list item
"""
class delete_user_wish_list_item(views.APIView): 
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        try:
            print(request.GET.get('product_name'))
            print(request.GET.get('product_id'))
            if request.GET.get('product_name') and request.GET.get('product_id'):

                product_id = int(request.GET.get('product_id').replace('wishlist',''))
                products_obj = Product.objects.filter(id= product_id).first()
                if products_obj:
                    user_wishlist_new_obj = UserWishList.objects.filter(
                            product = products_obj,
                            user = request.user
                        )
                    user_wishlist_new_obj.delete()
                response = {
                'message':'Succesfully Deleted',
                'data':"data",
                'status' : 200,  
                'url' : request.path,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                print("user id is not valid")
            response = {
                'message':'id is not found',
                'data':"data",
                'status' : 400,
                'url' : request.path,
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            print("delete user wish list",sys.exc_info())
            response = {
                    'message':'Something went wrong.',
                    'data':"data",
                    'status' : 500,
                    'url' : request.path,
            }
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Add User Cart list item
"""
class Add_user_cart_list_item(views.APIView): 
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        try:
            if request.GET.get('product_name') and request.GET.get('product_id'):
                product_id = int(request.GET.get('product_id'))
                size_obj = Size.objects.filter(name=request.GET.get('product_size')).first()
                products_obj = Product.objects.filter(id= product_id).first()
                if products_obj and size_obj:
                    quantity = 1
                    if int(request.GET.get('product_quantity')) > 1:
                        quantity =  request.GET.get('product_quantity')
                    # add condition here for availability of products and for size for product
                    # TODO here for availability and quantity
                    
                    try :
                        user_cartlist_new_obj = UserCart.objects.get(
                            product = products_obj,
                            user = request.user
                        )
                        user_cartlist_new_obj.qty += int(request.GET.get('product_quantity'))
                        user_cartlist_new_obj.size = size_obj
                        user_cartlist_new_obj.price = products_obj.price
                        user_cartlist_new_obj.save()
                        
                    except:
                        user_cartlist_new_obj1 = UserCart.objects.create(
                        product = products_obj,
                        user = request.user,
                        qty = quantity,
                        price = products_obj.price,
                        size = size_obj
                        )                        
                response = {
                'message':'Succesfully added',
                'data':"data",
                'status' : 200,  
                'url' : request.path,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                print("user id is not valid")
            response = {
                'message':'id is not found',
                'data':"data",
                'status' : 400,
                'url' : request.path,
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            print("user cart list",sys.exc_info())
            response = {
                    'message':'Something went wrong.',
                    'data':"data",
                    'status' : 500,
                    'url' : request.path,
            }
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Delete User cart list item
"""
class delete_user_cart_list_item(views.APIView): 
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        try:
            print(request.GET.get('product_name'))
            print(request.GET.get('product_id'))
            if request.GET.get('product_name') and request.GET.get('product_id'):

                product_id = int(request.GET.get('product_id'))
                products_obj = Product.objects.filter(id= product_id).first()
                
                if products_obj:
                    user_cartlist_new_obj = UserCart.objects.filter(
                            product = products_obj,
                            user = request.user
                        )

                    user_cartlist_new_obj.delete()
                response = {
                'message':'Succesfully Deleted',
                'status' : 200  
                }
                print('********',response)
                raise
                return Response(response,status=status.HTTP_200_OK)
            else:
                print("user id is not valid")
            response = {
                'message':'id is not found',
                'status' : 400
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            print("delete user wish list",sys.exc_info())
            response = {
                    'message':'Something went wrong.',
                    'status' : 500

            }
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
Filter Product
"""
class filter_product(views.APIView): 
    permission_classes = (AllowAny,) 

    def get(self, request):
        try:
            
            filter_ = json.loads(request.GET.get('filter'))
            print('>>>>>>>>>>>>>>>>>',filter_['design'])
            if filter_['design']:
                design_list = filter_['design']
                for each in design_list:
                    print("********************",each)
                    design_obj = ProductDesign.objects.filter(design__name = each)
                    print("********************",design_obj)

            raise
            if request.GET.get('product_name') and request.GET.get('product_id'):

                product_id = int(request.GET.get('product_id').replace('wishlist',''))
                products_obj = Product.objects.filter(id= product_id).first()
                if products_obj:
                    user_cartlist_new_obj = UserCart.objects.filter(
                            product = products_obj,
                            user = request.user
                        )
                    user_cartlist_new_obj.delete()
                response = {
                'message':'Succesfully Deleted',
                'data':"data",
                'status' : 200,  
                'url' : request.path,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                print("user id is not valid")
            response = {
                'message':'id is not found',
                'data':"data",
                'status' : 400,
                'url' : request.path,
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            print("delete user wish list",sys.exc_info())
            response = {
                    'message':'Something went wrong.',
                    'data':"data",
                    'status' : 500,
                    'url' : request.path,
            }
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)