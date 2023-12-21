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

    email = models.EmailField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=200)
    intro_text = models.CharField(blank=True, null=True, max_length=200)
    years_of_experience = models.PositiveIntegerField()
    completed_projects = models.PositiveIntegerField()
    countrywise_projects = models.PositiveIntegerField()
    logo = ResizedImageField(upload_to='logos',)

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
    pic = ResizedImageField(upload_to='skill', default="skill_default.png")


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

class Project(models.Model):
    profile_item = models.ForeignKey(ProfileItem, on_delete = models.CASCADE, related_name = 'projects')

    title = models.CharField(max_length = 200)
    tag = models.CharField(max_length = 255)
    pic = ResizedImageField(upload_to = 'project', default='project/project_default.png')
    description = models.TextField()
    link = models.CharField(max_length = 250)
    started_at = models.DateField(blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)

    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    profile_item = models.ForeignKey(ProfileItem, on_delete = models.CASCADE, related_name = 'testimonials')

    client = models.CharField(max_length= 150)
    client_role = models.CharField(max_length = 150)
    client_pic = ResizedImageField(upload_to = 'testimonial', default='testimonial/testimonial_default.png')
    company_name = models.CharField(max_length = 150)
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'project_testimonials')
    star = models.PositiveSmallIntegerField(validators = [MaxValueValidator(5)] )

    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return f'{self.text[:50]} by {self.client}'
    

class Service(models.Model):
    profile_item = models.ForeignKey(ProfileItem, on_delete = models.CASCADE, related_name = 'services')

    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    desc = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=200)
    pic = ResizedImageField(upload_to='service', default='service/service_default.png')
    completed_projects = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    
    full_name = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)
    budget = models.PositiveIntegerField(blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.full_name} - {self.text[0:50]}...'
    

class Social(models.Model):
    profile_item = models.ForeignKey(ProfileItem, on_delete = models.CASCADE, related_name = 'socials')

    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200, blank=True, null=True)
    pic = ResizedImageField(upload_to='social', default="socail_default.png")
    link = models.CharField(max_length = 250)

    def __str__(self):
        return self.title


    