from rest_framework import serializers
from core.models import Country, FilterCountry


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for country."""

    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ['id']

class FilterCountrySerializer(serializers.ModelSerializer):
    """Serializer for filters"""
    class Meta:
        model = FilterCountry
        fields = '__all__'
        read_only_fields = ['id']