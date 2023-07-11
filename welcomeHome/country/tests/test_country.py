from core.models import Country
from django.test import TestCase
from django.urls import reverse
from country.serializers import CountrySerializer
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

    def test_retrieve_country(self):
        """Test retrieving a list of countries."""
        create_country()
        create_country()
        res = self.client.get(COUNTRY_URL)
        countries = Country.objects.all().order_by("-id")
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_country_detail(self):
        """Test for detail of countries."""
        country = create_country()
        url = detail_url(country_id=country.id)
        res = self.client.get(url)
        serializer = CountrySerializer(country)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
