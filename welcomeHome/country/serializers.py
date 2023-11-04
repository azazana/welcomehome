from core.models import Country, CountryFilters
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for country."""

    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ['id']


class FilterCountrySerializer(serializers.ModelSerializer):
    """Serializer for filters"""

    class Meta:
        model = CountryFilters
        fields = '__all__'
        read_only_fields = ['id']
