from rest_framework import serializers

from userprofile.models import ProfileItem, Education, Skill, Testimonial, Project, Service, Contact, Social
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError as DjangoValidationError

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


class SocialSerializer(BaseProfileItemSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    # Phone number validation (optional)
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # Use CharField instead of IntegerField for the phone field
    phone = serializers.CharField(required=False, allow_null=True)
    # Email validation
    email = serializers.EmailField()

    # Budget validation (optional)
    budget = serializers.IntegerField(min_value=0, required=False, allow_null=True)

    class Meta:
        model = Contact
        fields = '__all__'

    def validate_phone(self, value):
        # Validate phone number using the RegexValidator
        if value == '':
            return None
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must start with '+'.")

        try:
            # Try to validate phone number using the RegexValidator
            self.phone_validator(value)
        except DjangoValidationError as e:
            # Catch the ValidationError from the RegexValidator and raise a new one with custom error message
            raise serializers.ValidationError("Invalid phone number format. " + str(e))
        
        return value


    def validate_budget(self, value):
        # Validate budget to ensure it's a positive integer
        if value is not None and value < 0:
            raise serializers.ValidationError("Budget must be a positive integer.")
        return value


    
