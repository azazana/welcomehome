from core import models
from django.test import TestCase


class ModelTests(TestCase):
    """Test models."""

    def test_create_country(self):
        country = models.Country.objects.create(
            country="Example country", code="MKHNM",
        )
        self.assertEqual(str(country), country.country)
