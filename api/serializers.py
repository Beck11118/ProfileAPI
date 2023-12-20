from rest_framework import serializers

from userprofile.models import ProfileItem, Education, Skill, Testimonial, Project, Service
from django.contrib.auth.models import User

class BaseProfileItemSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True

    def get_queryset(self):
        user = self.context['request'].user
        return ProfileItem.objects.filter(owner=user)

    


class EducationSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Education
        fields = "__all__"

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError('End date must be after start date')
        return data
    
    def validate_study(self, value):
        if not value.strip():
            raise serializers.ValidationError("Study field cannot be empty.")
        return value

    def validate_institution_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Institution name field cannot be empty.")
        return value

class SkillSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        

class ProfileItemSerializer(serializers.ModelSerializer):
    # educations = EducationSerializer(many=True, read_only=True)
    class Meta:
        model = ProfileItem
        exclude = ['owner']

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ProjectSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TestimonialSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class ServiceSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Service
        fields = "__all__"


    
