import django_filters
from .models import Country

class CountryModelFilter(django_filters.FilterSet):
    """Model for filtering country."""
    class Meta:
        model = Country
        fields = {
            'code':['exact','incontains']
        }
