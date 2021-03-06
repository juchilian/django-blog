from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.signals import user_logged_in
# Create your models here.

User = get_user_model()

def user_logged_in_receiver(request, user, *args, **kwargs):
    # print(request, user)
    pass

user_logged_in.connect(user_logged_in_receiver, sender=User)
# \copy blog_blogpost from 'C:\Users\juchi\Desktop\program\Python\django\django-blog\blog_app\data\django-blog-postgres.csv' with csv header