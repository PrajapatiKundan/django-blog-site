from django.db.models.signals import post_save #signal
from django.contrib.auth.models import User #sender of signal
from django.dispatch import receiver #receiver of signal
from .models import Profile
from django.db.models import ObjectDoesNotExist

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    #instance.profile.save()
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)