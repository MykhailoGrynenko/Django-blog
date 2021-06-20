from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extend default User model, so that users can have profile pictures"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
