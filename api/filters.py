import django_filters
from userprofile.models import ProfileItem, WorkExperience, Education

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


class EducationFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(
        fields = (
            ('start_date', 'start_date'),
            ('end_date', 'end_date')
        ),

        field_labels = {
            'start_date': 'Start date: ',
            'End_date': 'End date: ',
        }
    )

    class Meta:
        model = Education
        fields = ['start_date', 'end_date']


class WorkExperienceFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(
        fields = (
            ('start_date', 'start_date'),
            ('end_date', 'end_date')
        ),

        field_labels = {
            'start_date': 'Start date: ',
            'End_date': 'End date: ',
        }
    )
    
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='exact')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='exact')

    class Meta:
        model = WorkExperience
        fields = ['start_date', 'end_date']

