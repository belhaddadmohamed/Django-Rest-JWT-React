from django.db.models.signals import post_save 
from .models import User, Profile 


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )

def update_user(sender, instance, created, **kwargs):
    if not created:
        profile = instance
        user = profile.user
        user.username = profile.username
        user.email = profile.email
        user.save()



post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
