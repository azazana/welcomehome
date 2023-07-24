from core.models import (
    Country,
)
from rest_framework import viewsets
from country import serializers


class CountryViewSet(viewsets.ModelViewSet):
    """View for manage country"""
    serializer_class = serializers.CountrySerializer
    queryset = Country.objects.all()

    def get_queryset(self):
        return Country.objects.all().order_by("-id")
