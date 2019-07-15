from .models import MaintRequest
import django_filters

class MaintListFilter(django_filters.FilterSet):
    class Meta:
        model = MaintRequest
        fields = {
            'author': ['exact',],
            'title': ['icontains',],
            'priority': ['exact',],
            'status': ['exact',],
            'paid_by': ['exact',]
        }