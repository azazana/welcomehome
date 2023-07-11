from rest_framework import serializers
from core.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for country."""

    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ["id"]
