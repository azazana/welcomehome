from core.models import (
    Country,
)
from core.permissions import CustomDeletePermission
from country import serializers
from django.shortcuts import render
from rest_framework import viewsets


class CountryViewSet(viewsets.ModelViewSet):
    """View for manage country"""

    serializer_class = serializers.CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [CustomDeletePermission]

    def get_queryset(self):
        return Country.objects.all().order_by("-id")


def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', context={'countries': countries},)


def details(request, id):
    country = Country.objects.get(id=id)
    return render(request, 'details.html', context={'country': country},)
