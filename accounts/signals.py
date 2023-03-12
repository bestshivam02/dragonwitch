from multiprocessing import context
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.conf import settings
from django.core.mail import send_mail
import sys
from django.template.loader import render_to_string

@receiver(post_save,sender=User)
def user_save(sender,instance,created , **kwargs):
    if created:
        # send e-mail
        try:
            subject = f'Welcome {instance.email} To Resumes Helper'
            context = {}
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail( subject,
             render_to_string('email/email.txt',context), 
             email_from, 
             recipient_list)
        except:
            print('>>>>>>>',sys.exc_info())
            pass