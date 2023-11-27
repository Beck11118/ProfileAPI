import django_filters
from userprofile.models import ProfileItem

class ProfileItemFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('skills', 'skills'),
        ),

        field_labels = {
            'name': 'User name: ',
            'skills': 'User skills: ',
        }

    )

    class Meta:
        model = ProfileItem
        fields = {
            'name': ['exact', 'icontains'],
            'skills': ['exact', 'icontains']
        }