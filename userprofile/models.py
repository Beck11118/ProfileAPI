from django.db import models
from django.contrib.auth.models import User

class ProfileItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
