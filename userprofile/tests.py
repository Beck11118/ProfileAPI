from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import ProfileItem

class ProfileItemAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile_item_data = {
            'name': 'John Doe', 
            'bio': 'A software developer',
            'skills': 'Python, Django, Javascript',
            'contact_info': 'beck@gmail.com',
        }
        self.url = reverse('api:profileitem-list')
    def test_create_profile_item(self):
        response = self.client.post(self.url, self.profile_item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProfileItem.objects.count(), 1)
        self.assertEqual(ProfileItem.objects.get().name, 'John Doe')
    
    def test_invalid_skills_format(self):
        invalid_data = {
            'name': 'Jane Doe',
            'bio': 'Another developer.',
            'skills': 'Python;Django;JavaScript',  # Invalid format with semicolons
            'contact_info': 'jane@example.com',
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ProfileItem.objects.count(), 0)

