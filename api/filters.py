import django_filters
from userprofile.models import ProfileItem

class ProfileItemFilter(django_filters.FilterSet):
    # o = django_filters.OrderingFilter(
    #     fields=(
    #         ('name', 'name'),
    #     ),

    #     field_labels = {
    #         'name': 'User name: ',
    #     }

    # )

    class Meta:
        model = ProfileItem
        fields = {
            # 'name': ['exact', 'icontains'],
        }