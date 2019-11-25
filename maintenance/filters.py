from .models import MaintRequest
import django_filters

class MaintListFilter(django_filters.FilterSet):

    CHOICES = [('newest', 'Newest'),
               ('oldest', 'Oldest')]
               

    ordering = django_filters.ChoiceFilter(label=False,  choices=CHOICES, method='order_by', empty_label='Sort')

    class Meta:
        model = MaintRequest
        fields = {
            'author': ['exact',],
            'title': ['icontains',],
            'priority': ['exact',],
            'status': ['exact',],
            'paid_by': ['exact',]
        }

    def order_by(self, queryset, name, value):
        expression = '-date_raised' if value == 'newest' else 'date_raised'
        return queryset.order_by(expression)