from .models import MaintRequest
import django_filters


class MaintListFilter(django_filters.FilterSet):
    """
    Search form for maintenance request list
    """

    # choices for maintenance list ordering
    CHOICES = [('newest', 'Newest'),
               ('oldest', 'Oldest')]

    ordering = django_filters.ChoiceFilter(label=False, choices=CHOICES, method='order_by', empty_label='Sort')

    class Meta:
        model = MaintRequest
        fields = {
            'author': ['exact', ],
            'title': ['icontains', ],
            'priority': ['exact', ],
            'status': ['exact', ],
            'paid_by': ['exact', ]
        }

    # method for sort form
    def order_by(self, queryset, name, value):
        expression = '-date_raised' if value == 'newest' else 'date_raised'
        return queryset.order_by(expression)
