from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.TextField()
    preferences = models.TextField()

class ProfilePicture(models.Model):
    profile = models.ForeignKey(Profile, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures/')
