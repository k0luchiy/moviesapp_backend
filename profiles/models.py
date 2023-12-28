from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default="profile_default_image.jpg", upload_to="profile_images/")
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        IMAGE_WIDTH = 300
        IMAGE_HEIGHT= 500

        img = Image.open(self.image.path)
        if img.width > IMAGE_WIDTH or img.height > IMAGE_HEIGHT: 
            img.thumbnail((IMAGE_WIDTH,IMAGE_HEIGHT))
            img.save(self.image.path)

