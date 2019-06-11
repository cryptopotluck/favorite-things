
from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    profile_image = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profile/2019/04/29/default.png', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
