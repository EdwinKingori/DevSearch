from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField()
