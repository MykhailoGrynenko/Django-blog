from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Run this function every time a user is created.
         So that, whenever a user is created, a default profile is created as well."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    """Run this function every time a user is created.
         Create a safe profile function that saves user's profile every time a user object gets saved."""
    instance.profile.save()
