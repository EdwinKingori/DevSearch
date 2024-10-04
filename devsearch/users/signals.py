from django.contrib.auth.models import User
from .models import Profile


# importing signals
from django.db.models.signals import post_save, post_delete
# importing decorators to trigger the signals above
from django.dispatch import receiver


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

    print("Deleting user...")


post_save.connect(createProfile, sender=User)


post_delete.connect(deleteUser, sender=Profile)
