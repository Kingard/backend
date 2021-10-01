from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state_of_residence = models.CharField(max_length= 120, default='location')

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()    

class Product(TimeStampedModel):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length = 300)
    image = models.ImageField(upload_to="image")
    seller = models.ForeignKey(Users, default='Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Buyer(TimeStampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    location = models.CharField(max_length=120)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    
