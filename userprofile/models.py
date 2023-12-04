from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

from django.core.validators import MaxValueValidator

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
    
class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    icon = models.CharField(max_length=255)

    profile_item = models.ForeignKey(ProfileItem, on_delete=models.CASCADE, related_name='skills')    
    
    # provide additional details or context about each skill.
    # description = models.TextField(blank=True, null=True)

    # categorizing skills into different types or categories.
    # category = models.CharField(max_length=255, blank=True, null=True)

    # store a link to a certification or some form of proof for the skill.
    # certification_link = models.URLField(blank=True, null=True)

    # add tags or keywords to skills for easier searching and categorization. 
    # tags = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name
    


