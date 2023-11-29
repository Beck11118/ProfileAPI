from rest_framework import serializers

from userprofile.models import ProfileItem, Education
from django.contrib.auth.models import User


class EducationSerializer(serializers.ModelSerializer):
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

class ProfileItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileItem
        fields = "__all__"

    
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
    
