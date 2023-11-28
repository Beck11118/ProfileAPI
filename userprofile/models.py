from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class ProfileItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    main_quote = models.CharField(max_length=255, default="Make it work, make it right, make it fast")
    bio = models.TextField()
    short_bio = models.TextField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    pic = ResizedImageField(upload_to = 'user_pic', default = 'user_pic/default.png')

    def __str__(self):
        if self.owner.first_name != '':
            return f'{self.owner.first_name} {self.owner.last_name}'
        return self.owner.username
    
class Education(models.Model):
    start_date = models.DateField()
    end_date= models.DateField(null=True, blank=True)
    study = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)

    profile_item = models.ForeignKey(ProfileItem, on_delete=models.CASCADE, related_name='educations')    

    def __str__(self):
        return f'{self.study} at {self.institution_name}'
    
    