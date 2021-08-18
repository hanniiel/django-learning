from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

#@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
   


def createProfile(sender, instance, created, **kwargs):
     if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username= user.username,
            name= user.first_name,
            email = user.email
        )

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)