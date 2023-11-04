from core.models import Country, CountryFilters
from country.serializers import CountrySerializer
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import override
from rest_framework import status
from rest_framework.test import APIClient

COUNTRY_URL = reverse("country:country-list")


def detail_url(country_id):
    """Create and return a country detail URL."""
    return reverse("country:country-detail", args=[country_id])


def create_country(**params: dict):
    """Create and return a country."""
    defaults = {
        "country": "Country test",
        "code": "MDETS",
        "countryDescription": "Country description Test",
        "language": "Country language",
    }
    defaults.update(params)
    country = Country.objects.create(**defaults)

    return country


class CountryAPITests(TestCase):
    """Test API requests."""

    def setUp(self):
        self.client = APIClient()
        self.country = create_country()

    def test_retrieve_country(self):
        """Test retrieving a list of countries."""
        create_country()
        with override('uk'):
            res = self.client.get(COUNTRY_URL, )
            countries = Country.objects.all().order_by("-id")
            serializer = CountrySerializer(countries, many=True)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, serializer.data)

    def test_get_country_detail(self):
        """Test for detail of countries."""
        with override('uk'):
            url = detail_url(country_id=self.country.id)
            res = self.client.get(url)
            serializer = CountrySerializer(self.country)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, serializer.data)

    def _assert_data_by_filters(self, response):
        expected_data = CountrySerializer([self.country], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_filter_countries_by_code(self):
        """Test for countries with filter code"""
        with override('uk'):
            response = self.client.get(COUNTRY_URL, {"code": "MDETS"})
            self._assert_data_by_filters(response)

    def test_filter_by_costOfBirthInStateClinic(self):
        default_filters = {
            "costOfBirthInStateClinic": "безкоштовно",
            "specialConditionsForUkrainians": "ні",
            "citizenshipByBirth": True,
            "minimumDurationOfPaidMaternityLeave": "0 - 5",
            "freeKindergarten": True,
            "hoursPerWeekChildrenFreePreschoolEducation": "0 - 10",
            "ageFreePreschoolEducation": "1",
            "costOfChildcareFromUSDPerMonth": 50,
        }
        CountryFilters.objects.create(country=self.country, **default_filters)
        with override('uk'):
            for key, value in default_filters.items():
                response = self.client.get(COUNTRY_URL, {key: value})
                self._assert_data_by_filters(response)
        # with override('ru')
        #     default_filters = {
        #         "costOfBirthInStateClinic": "бесплатно",
        #         "specialConditionsForUkrainians": "нет",
        #     }
        #     CountryFilters.objects.create(country=self.country,
        #     **default_filters)
        #     for key, value in default_filters.items():
        #         response = self.client.get(COUNTRY_URL, {key: value})
        #         self._assert_data_by_filters(response)
