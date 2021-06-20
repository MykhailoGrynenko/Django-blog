from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Extend default User model, so that users can have profile pictures"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    # This doesn't work with S3 bucket
    # def save(self, *args, **kwargs):
    #     """Resize an image to smaller size."""
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
