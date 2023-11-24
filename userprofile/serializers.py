from rest_framework import serializers

from .models import ProfileItem
from django.contrib.auth.models import User

class ProfileItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileItem
        fields = "__all__"

    def validate_skills(self, value):
        # Custom validation for skills (comma-separated)
        skills_list = [skill.strip() for skill in value.split(',')]
        
        # Ensure there is at least one skill
        if not any(skills_list):
            raise serializers.ValidationError("Skills field must contain at least one skill.")
        
        # Ensure all skills are separated by commas
        if len(skills_list) > 1 and any((':' in skill or ';' in skill) for skill in skills_list[1:]):
            raise serializers.ValidationError("Skills must be separated by commas.")
        
        return ','.join(skills_list)
    
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