from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(default='profile.jpg', upload_to='profile_pic')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
