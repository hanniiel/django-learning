from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

#@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('saved')

