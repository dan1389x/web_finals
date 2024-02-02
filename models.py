from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass

#uploaded images
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='static/images/user')
