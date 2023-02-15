import logging
from django.db.models.signals import post_save
from author_api.settings.base import AUTH_USER_MODEL
from django.dispatch import receiver

from core_apps.profiles.models import Profile

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    logging.info(f"{instance}'s profile created successfully")