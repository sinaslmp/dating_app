from django.contrib.auth.models import AbstractUser
from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
