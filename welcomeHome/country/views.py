from core.models import (
    Country, CountryFilters,
)
from core.permissions import CustomDeletePermission
from country import serializers
from django.shortcuts import render
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiTypes
)
from rest_framework import viewsets


@extend_schema_view(
    list=extend_schema(
        parameters=[OpenApiParameter(
            'code',
            OpenApiTypes.STR,
            description='Comma separated list of country codes',
        ),
            OpenApiParameter(
                'costOfBirthInStateClinic',
                OpenApiTypes.STR,
                description='Comma separated list of cost of birth in state clinics',
            ),
            OpenApiParameter(
                'citizenshipByBirth',
                OpenApiTypes.BOOL,
                description='Citizenship for newborn baby',
            ),
            OpenApiParameter(
                'specialConditionsOfDepositForUkrainians',
                OpenApiTypes.STR,
                description='special conditions for Ukrainians',
            ),
            OpenApiParameter(
                'freeKindergarten',
                OpenApiTypes.BOOL,
                description='there is free kindergarten',
            ),
            OpenApiParameter(
                'ageFreePreschoolEducation',
                OpenApiTypes.STR,
                description='age of free preschool education',
            ),
            OpenApiParameter(
                'hoursPerWeekChildrenFreePreschoolEducation',
                OpenApiTypes.STR,
                description='hours per week children free preschool education',
            ),
            OpenApiParameter(
                'costOfChildcareFromUSDPerMonth',
                OpenApiTypes.STR,
                description='cost of childcare in USD per month',
            ),

        ], ))
class CountryViewSet(viewsets.ModelViewSet):
    """View for manage country"""

    serializer_class = serializers.CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [CustomDeletePermission]

    def _params_to_str(self, qs, type = str):
        """Convert a str to list of strings."""
        if qs:
            if type == str:
                return [strings for strings in qs.split(',')]
            elif qs and type != str:
                return [int(interger) for interger in qs.split(',')]
        return qs

    def _get_queryset_with_filter(self, queryset, dict_param: dict, field):
        """Get queryset with filter."""
        if field:
            country_filter = CountryFilters.objects.all()
            country_filter = country_filter.filter(
                **dict_param)
            queryset = queryset.filter(
                id__in=country_filter.values_list("country", flat=True))
        return queryset
    def _get_param_from_request(self,param):
        return  self.request.query_params.get(param)
    def get_queryset(self):
        """Retrieve countries with filter."""
        codes = self._get_param_from_request("code")
        costOfBirthInStateClinic = self._get_param_from_request("costOfBirthInStateClinic")
        citizenshipByBirth = self._get_param_from_request("citzenshipByBirth")
        specialConditionsForUkrainians = self._get_param_from_request("specialConditionsOfDepositForUkrainians")
        minimumDurationOfPaidMaternityLeave = self._get_param_from_request("minimumDurationOfPaidMaternityLeave")
        freeKindergarten = self._get_param_from_request("freeKindergarten")
        hoursPerWeekChildrenFreePreschoolEducation = self._get_param_from_request("hoursPerWeekChildrenFreePreschoolEducation")
        ageFreePreschoolEducation=self._get_param_from_request("ageFreePreschoolEducation")
        costOfChildcareFromUSDPerMonth=self._get_param_from_request("costOfChildcareFromUSDPerMonth")
        queryset = self.queryset
        if codes:
            queryset = queryset.filter(code__in=self._params_to_str(codes))
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {"costOfBirthInStateClinic__in": self._params_to_str(
                                                      costOfBirthInStateClinic),
                                                  }, field=costOfBirthInStateClinic
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {"minimumDurationOfPaidMaternityLeave__in": self._params_to_str(
                                                      minimumDurationOfPaidMaternityLeave),
                                                  }, field=minimumDurationOfPaidMaternityLeave
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {
                                                      "hoursPerWeekChildrenFreePreschoolEducation__in": self._params_to_str(
                                                          hoursPerWeekChildrenFreePreschoolEducation),
                                                  }, field=freeKindergarten
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {
                                                      "ageFreePreschoolEducation__in": self._params_to_str(
                                                          ageFreePreschoolEducation),
                                                  }, field=ageFreePreschoolEducation
                                                  )


        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {
                                                      "citizenshipByBirth": citizenshipByBirth.lower() == "true" if isinstance(
                                                          citizenshipByBirth, str) else None,
                                                  }, field=citizenshipByBirth
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {"specialConditionsForUkrainians": specialConditionsForUkrainians,
                                                   }, field=specialConditionsForUkrainians
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {"freeKindergarten": freeKindergarten.lower() == "true" if isinstance(
                                                      freeKindergarten, str) else None,
                                                   }, field=freeKindergarten
                                                  )
        queryset = self._get_queryset_with_filter(queryset,
                                                  dict_param=
                                                  {"costOfChildcareFromUSDPerMonth__in": self._params_to_str(
                                                          costOfChildcareFromUSDPerMonth),
                                                   }, field=costOfChildcareFromUSDPerMonth
                                                  )
        return queryset.order_by("-id")


def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', context={'countries': countries}, )


def details(request, id):
    country = Country.objects.get(id=id)
    return render(request, 'details.html', context={'country': country}, )
