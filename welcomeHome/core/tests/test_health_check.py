"""
Test for checking health API.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.utils.translation import activate

class HealthCheckTests(TestCase):
    """Test the health check API."""

    def test_health_check(self):
        language_code = 'uk'
        activate(language_code)  # Set the active language

        # Create a client with Accept-Language header
        headers = {'HTTP_ACCEPT_LANGUAGE': language_code}

        url = reverse("health-check")
        client = APIClient()
        res = client.get(url, **headers)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
