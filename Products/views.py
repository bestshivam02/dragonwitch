from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

"""
Product Dashboard
"""
@login_required
def productdashboard(request):
	all_products = Product.objects.all()
	all_category = Category.objects.all()
	empty_products_list = []
	count = 0
	for each in all_category:

		each_product = Product.objects.filter(productcategory__category = each)
		empty_list = []
		for each1 in each_product:
			empty_list.append(each1)
		empty_products_list.append({
			each.id:empty_list
		})

	return render(request, 'admin/products/eco-products.html',{"all_products":all_products,'all_category':all_category,"products_list":empty_products_list})

@login_required
def addproductdashboard(request):

	all_category = Category.objects.all()
	all_size = Size.objects.all()
	all_material = Material.objects.all()
	all_color = Color.objects.all()
	all_design = Design.objects.all()
	context = {
		'all_category':all_category,
		'all_size':all_size,
		'all_material':all_material,
		'all_color':all_color,
		'all_design':all_design,
		}
	if request.method=='POST':

		if Product.objects.filter(name=request.POST.get('name', None)):
			messages.error(request, 'product name is already exists.')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not request.POST.get('name'):
			messages.error(request, 'Please enter name.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

		if not request.FILES.get('image'):
			messages.error(request, 'Please enter image.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

		if not request.POST.get('category'):
			messages.error(request, 'Please enter category.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

		category_obj = Category.objects.filter(name = request.POST.get('category', None)).first()

		new_product_obj =  Product.objects.create(
			name =  request.POST.get('name'),
			slug =  request.POST.get('name'),
			# image =  request.FILES.get('image'),
			price =  request.POST.get('price'),
			description =  request.POST.get('description'),
			quantity =  request.POST.get('quantity'),
			discount_price =  request.POST.get('discount_price'),
		)

		if request.FILES.getlist('image') and new_product_obj:
			images = request.FILES.getlist('image')
			if images:
				new_product_obj.image = images[0]
				new_product_obj.save()
				for each in images:
					product_image_obj = ProductImages.objects.create(
						product = new_product_obj,
						image = each
					)
		quantity = 0
		if request.POST.get('quantity'):
			quantity = request.POST.get('quantity')

		add__to_category = ProductCategory.objects.create(
				product = new_product_obj,
				category = category_obj,
				quantity = quantity,
				status = True,
		)
		add_to_product_rating = ProductRating.objects.create(
				product = new_product_obj,
				rating_star = 0
		)

		for each in all_design:
			if each.name in request.POST:

				design_obj = Design.objects.filter(name = each.name)
				if design_obj :
					add_to_design = ProductDesign.objects.create(
						product =  new_product_obj,
						design = design_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_size:
			if each.name in request.POST:

				size_obj = Size.objects.filter(name = each.name)
				if size_obj :
					add_to_size = ProductSize.objects.create(
						product =  new_product_obj,
						size = size_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_material:
			if each.name in request.POST:

				material_obj = Material.objects.filter(name = each.name)
				if material_obj :
					add_to_material = ProductMaterial.objects.create(
						product =  new_product_obj,
						material = material_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_color:
			if each.name in request.POST:

				color_obj = Color.objects.filter(name = each.name)
				if color_obj :
					add_to_color = ProductColor.objects.create(
						product =  new_product_obj,
						color = color_obj.first(),
						quantity = quantity,
						status = True
					)

		if add__to_category:
			messages.error(request, 'Product Added Succesfully.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


	return render(request, 'admin/products/eco-product-add.html',context)

@login_required
def editproductdashboard(request,pk):

	product_obj = Product.objects.get(pk=pk)
	all_category = Category.objects.all()
	all_size = Size.objects.all()
	all_material = Material.objects.all()
	all_color = Color.objects.all()
	all_design = Design.objects.all()

	product_size = ProductSize.objects.filter(product = product_obj)
	product_material = ProductMaterial.objects.filter(product = product_obj)
	product_color = ProductColor.objects.filter(product = product_obj)
	product_design = ProductDesign.objects.filter(product = product_obj)

	context = {
		'product':product_obj,
		'all_category':all_category,
		'all_size':all_size,
		'all_material':all_material,
		'all_color':all_color,
		'all_design':all_design,
		'product_size':product_size,
		'product_material':product_material,
		'product_color':product_color,
		'product_design':product_design,
	}

	if request.method=='POST' and product_obj:

		category_obj = Category.objects.filter(name = request.POST.get('category', None)).first()
		quantity = 0
		if request.POST.get('quantity'):
			quantity = int(request.POST.get('quantity'))

		if category_obj:
			try:
				add__to_category = ProductCategory.objects.get(
					product = product_obj,
					status = True
				)

				add__to_category.category = category_obj
				add__to_category.quantity = quantity
				add__to_category.save()
			except :

				add__to_category = ProductCategory.objects.create(
					product = product_obj,
					category = category_obj,
					quantity = quantity,
					status = True
				)
		else:
			messages.error(request, 'category is invalid.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
		if request.POST.get('name'):
			product_obj.name = request.POST.get('name')

		if request.FILES.getlist('image'):
			images = request.FILES.getlist('image')
			if images:
				product_obj.image = images[0]
				product_obj.save()
				all_product_images = ProductImages.objects.filter(product = product_obj)
				all_product_images.delete()
				for each in images:
					product_image_obj = ProductImages.objects.create(
						product = product_obj,
						image = each
					)

		if request.POST.get('price'):
			product_obj.price = request.POST.get('price')

		if request.POST.get('discount_price'):
			product_obj.discount_price = request.POST.get('discount_price')

		if request.POST.get('additional_information'):
			product_obj.additional_information = request.POST.get('additional_information')

		if request.POST.get('quantity'):
			product_obj.quantity = quantity

		if request.POST.get('description'):
			product_obj.description = request.POST.get('description')

		product_material_all = ProductMaterial.objects.filter(product =  product_obj)
		product_material_all.delete()

		product_design_all = ProductDesign.objects.filter(product =  product_obj)
		product_design_all.delete()

		product_size_all = ProductSize.objects.filter(product =  product_obj)
		product_size_all.delete()

		product_color_all = ProductColor.objects.filter(product =  product_obj)
		product_color_all.delete()

		for each in all_design:
			if each.name in request.POST:

				design_obj = Design.objects.filter(name = each.name)
				if design_obj :
					add_to_design = ProductDesign.objects.create(
						product =  product_obj,
						design = design_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_size:
			if each.name in request.POST:

				size_obj = Size.objects.filter(name = each.name)
				if size_obj :
					add_to_size = ProductSize.objects.create(
						product =  product_obj,
						size = size_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_material:
			if each.name in request.POST:

				material_obj = Material.objects.filter(name = each.name)

				if material_obj :
					add_to_material = ProductMaterial.objects.create(
						product =  product_obj,
						material = material_obj.first(),
						quantity = quantity,
						status = True
					)

		for each in all_color:
			if each.name in request.POST:
				color_obj = Color.objects.filter(name = each.name)
				if color_obj :
					add_to_color = ProductColor.objects.create(
						product =  product_obj,
						color = color_obj.first(),
						quantity = quantity,
						status = True
					)

		product_obj.save()
		return redirect('Products:product_dashboard')
	return render(request, 'admin/products/eco-product-edit.html',context)

@login_required
def deleteproductdashboard(request,pk):

	product_obj = Product.objects.get(pk=pk)
	if request.method=='POST' and product_obj:
		product_obj.delete()
		return redirect('Products:product_dashboard')
	return render(request, 'admin/products/eco-product-edit.html',{'product':product_obj})


"""
Category Dashboard
"""

@login_required
def category_dashboard(request):
	all_category = Category.objects.all()
	return render(request, 'admin/products/eco-category.html',{"all_category":all_category})


@login_required
def addcategorydashboard(request):

	if request.method=='POST':
		if Category.objects.filter(name=request.POST.get('name', None)):
			messages.error(request, 'category name is already exists.')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not request.POST.get('name'):
			messages.error(request, 'Please enter name.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

		new_category_obj =  Category.objects.create(
			name =  request.POST.get('name'),
			slug =  request.POST.get('name'),
		)

		if new_category_obj:
			messages.error(request, 'Category Added Succesfully.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

	return render(request, 'admin/products/eco-category-add.html')

@login_required
def editcategorydashboard(request,pk):

	category_obj = Category.objects.get(pk=pk)

	if request.method=='POST' and category_obj:
		if request.POST.get('name'):
			category_obj.name = request.POST.get('name')
			category_obj.slug = request.POST.get('name')

		category_obj.save()
		return redirect('Products:category_dashboard')
	return render(request, 'admin/products/eco-category-edit.html',{'category':category_obj})

@login_required
def deletecategorydashboard(request,pk):

	category_obj = Category.objects.get(pk=pk)
	if request.method=='POST' and category_obj:
		category_obj.delete()
		return redirect('Products:category_dashboard')
	return render(request, 'admin/products/eco-category-edit.html',{'category':category_obj})


"""
Product Type Dashboard
"""
@login_required
def producttypedashboard(request):
	all_products = Product.objects.all()
	all_category = Category.objects.all()
	empty_products_list = []
	all_size_obj = Size.objects.all()
	all_material_obj = Material.objects.all()
	all_color_obj = Color.objects.all()
	all_Design_obj = Design.objects.all()

	context = {
		"all_size_obj":all_size_obj,
		"all_material_obj":all_material_obj,
		"all_color_obj":all_color_obj,
		"all_Design_obj":all_Design_obj,
	}

	return render(request, 'admin/products/eco-product-type.html',context)


@login_required
def add_producttypedashboard(request):

	if request.method=='POST':

		if not request.POST.get('name'):
			messages.error(request, 'Please enter name.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

		if request.POST.get('type'):
			if request.POST.get('type') == 'Design':
				new_category_obj =  Design.objects.create(
					name =  request.POST.get('name'),
					slug =  request.POST.get('name'),
				)
			elif request.POST.get('type') == 'Material':
				new_category_obj =  Material.objects.create(
					name =  request.POST.get('name'),
					slug =  request.POST.get('name'),
				)
			elif request.POST.get('type') == 'Size':
				new_category_obj =  Size.objects.create(
					name =  request.POST.get('name'),
					slug =  request.POST.get('name'),
				)
			elif request.POST.get('type') == 'Color':
				new_category_obj =  Color.objects.create(
					name =  request.POST.get('name'),
					slug =  request.POST.get('name'),
				)
			else:
				pass
		if new_category_obj:
			messages.error(request, 'Category Added Succesfully.')
			return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

	return render(request, 'admin/products/eco-product-type-add.html')

"""
Update Product review
"""
def update_product_review(request,pk):
	context = {}

	if request.user.is_authenticated:

		if request.method=="POST":
			print("****************",request.POST)

			try:
				product_obj = Product.objects.get(id=pk)
				try:
					
					product_review_obj_old = ProductReview.objects.get(product = product_obj,user =  request.user)
					if request.POST.get('title'):
						product_review_obj_old.title = request.POST.get('title',None)
					product_review_obj_old.review = request.POST.get('review',None)
					product_review_obj_old.rating_star = request.POST.get('rating_star',None)
					product_review_obj_old.save()
				except:
					product_review_obj_new = ProductReview.objects.create(
						product = product_obj,
						user =  request.user
						)
					if request.POST.get('title'):
						product_review_obj_new.title = request.POST.get('title',None)
					product_review_obj_new.review = request.POST.get('review',None)
					product_review_obj_new.rating_star = request.POST.get('rating_star',None)
					product_review_obj_new.save()
				
				return redirect('frontend:each_products' , pk=pk)
			except:
				messages.error(request, 'Product is not somthing.')
				return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
		return redirect('frontend:profile')
	else:
		return redirect('frontend:index')

"""
Apply Promo Code
"""
def apply_promo(request):
	context = {}

	if request.user.is_authenticated:

		if request.method=="POST" and request.POST.get('promo_code'):
			
			promo_code_obj = PromoCode.objects.filter(name=request.POST.get('promo_code'),is_active=True).first()
			print("********************",promo_code_obj)

			try:
				user_promo_code = None
				if promo_code_obj:
					user_promo_code = UserPromoCode.objects.filter(user=request.user,promocode=promo_code_obj)
				else:
					messages.error(request, 'Promo code is not valid')
					return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
				if user_promo_code:

					# user already used this promo code
					print('its exists')
					messages.error(request, 'You already used promo code.')
					return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
				else:
					#apply promo code
					print('hello')
					user_cart_obj = UserCart.objects.filter(user= request.user)
					for each in user_cart_obj:
						price = each.price
						discoun_ammount = (promo_code_obj.percentage * price)/100
						if discoun_ammount > 0:
							each.price = discoun_ammount
							each.save()
							user_apply_promo_code = UserPromoCode.objects.create(
								promocode = promo_code_obj,
							    user = request.user
							)
						else:
							messages.error(request, 'You already used promo code. 0')
							return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
			except Exception as e:
				print("error >",e)
				messages.error(request, 'Product is not somthing.')
				return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
		return redirect('frontend:usercheckout')
	else:
		return redirect('frontend:index')

"""
Order Dashboard
"""
@login_required
def order_dashoard(request):
	context ={}
	if request.user.is_authenticated and request.user.role_id == 1:
		order_history_obj = UserOrderHistory.objects.filter(has_paid = True)
		# Paginator
		paginator = Paginator(order_history_obj, 15)
		page_number = request.GET.get('page', 1)
		try:
			page_obj = paginator.get_page(page_number)  # returns the desired page object
		except PageNotAnInteger:
			# if page_number is not an integer then assign the first page
			page_obj = paginator.page(1)
		except EmptyPage:
			# if page is empty then return last page
			page_obj = paginator.page(paginator.num_pages)
		context['all_order_history'] = page_obj
		return render(request, 'admin/order/all_order.html',context)
	else:
		return redirect('frontend:index')

"""
Order Not Deliverd Dashboard
"""
@login_required
def order_not_delivered_dashboard(request):
	context ={}
	if request.user.is_authenticated and request.user.role_id == 1:
		order_history_obj = UserOrderHistory.objects.filter(has_paid = True,has_delivered = False)
		# Paginator
		paginator = Paginator(order_history_obj, 15)
		page_number = request.GET.get('page', 1)
		try:
			page_obj = paginator.get_page(page_number)  # returns the desired page object
		except PageNotAnInteger:
			# if page_number is not an integer then assign the first page
			page_obj = paginator.page(1)
		except EmptyPage:
			# if page is empty then return last page
			page_obj = paginator.page(paginator.num_pages)
		context['all_order_history'] = page_obj
		return render(request, 'admin/order/order_not_delivered.html',context)
	else:
		return redirect('frontend:index')

"""
Order Deliverd  Dashboard
"""

def order_delivered_dashboard(request):
	context ={}
	if request.user.is_authenticated and request.user.role_id == 1:
		order_history_obj = UserOrderHistory.objects.filter(has_paid = True,has_delivered = True)
		# Paginator
		paginator = Paginator(order_history_obj, 15)
		page_number = request.GET.get('page', 1)
		try:
			page_obj = paginator.get_page(page_number)  # returns the desired page object
		except PageNotAnInteger:
			# if page_number is not an integer then assign the first page
			page_obj = paginator.page(1)
		except EmptyPage:
			# if page is empty then return last page
			page_obj = paginator.page(paginator.num_pages)
		context['all_order_history'] = page_obj
		return render(request, 'admin/order/order_delivered.html',context)
	else:
		return redirect('frontend:index')

"""
Update Delivery status  Dashboard
"""
def update_order_delivery_status_dashboard(request,pk):

	if request.user.is_authenticated and request.user.role_id == 1:
		order_history_obj = UserOrderHistory.objects.filter(id=pk,has_paid = True).first()
		user_custom_order = UserCustomProductOrder.objects.filter(order_history = order_history_obj).first()
		context = {
			'order_history_obj':order_history_obj,
			'user_custom_order':user_custom_order,
		}
		if request.method=='POST' and order_history_obj:
			if request.POST.get('has_delivered'):
				order_history_obj.has_delivered = True
				order_history_obj.save()
			return redirect('Products:order_dashoard')
		else:
			return render(request, 'admin/order/update_order.html',context)
	else:
		return redirect('frontend:index')