from multiprocessing import context
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductReview,ProductRating
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

@receiver(post_save,sender=ProductReview)
def user_save(sender,instance,created , **kwargs):
    # if created:
        # send message
        try:
            print("insatance",type(instance))
            print("insatance",instance)
            value = float(instance.rating_star)
            prodcut_revie_count = ProductReview.objects.filter(product = instance.product)
            total_review = 0
            for each in prodcut_revie_count:
                total_review += each.rating_star
            count = prodcut_revie_count.count()
            print('total_review',total_review)
            print('****************',value)
            print('****************',prodcut_revie_count)
            
            try:
					
                product_rating_old = ProductRating.objects.get(product = instance.product)
                product_rating_old.rating_star = (total_review + value )/(count+1)
                product_rating_old.save()
                print('(((((((((((((((',product_rating_old.rating_star)

            except Exception as e:
                print('>>>>>>>',e)
                product_rating_new = ProductRating.objects.create(
                    product = instance.product,
                    )
                product_rating_new.rating_star = value
                product_rating_new.save()
                print('(((((((((((((((',product_rating_new.rating_star)
        except Exception as e:
            print('>>>>>>>',e)
            pass