from core.models import (
    Country,
)
from core.permissions import CustomDeletePermission
from country import serializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, schema
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiTypes
)


@extend_schema_view(
    list=extend_schema(
        parameters=[OpenApiParameter(
            'code',
            OpenApiTypes.STR,
            deprecated='Comma separated list of codes',
        )]
    )
)
class CountryViewSet(viewsets.ModelViewSet):
    """View for manage country"""

    serializer_class = serializers.CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [CustomDeletePermission]

    def _params_to_str(self, qs):
        """Convert a str to list of strings."""
        return [strings for strings in qs.split(',')]

    def get_queryset(self):
        """Retrieve countries with filter."""
        codes = self.request.query_params.get("code")
        queryset = self.queryset
        if codes:
            codes_without_comma = self._params_to_str(codes)
            print(codes_without_comma)
            queryset = queryset.filter(code__in=codes_without_comma)
        return queryset.order_by("-id")


def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', context={'countries': countries}, )


def details(request, id):
    country = Country.objects.get(id=id)
    return render(request, 'details.html', context={'country': country}, )
