import django_filters
from .models import ProfileItem

class ProfileItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProfileItem
        fields = {
            'name': ['exact', 'icontains'],
            'skills': ['exact', 'icontains']
        }