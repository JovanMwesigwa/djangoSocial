from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (
    post_save
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='profile_followers', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Profile for {}'.format(self.first_name)


@receiver(post_save, sender=User)
def create_profile_signal(sender, created, instance, *args, **kwargs):
    if created:
        profile = Profile()
        profile.user = instance
        profile.first_name = instance.username
        profile.save()
    else:
        print("An error occured while creating your profile")
