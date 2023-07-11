"""
Test for checking health API.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    """Test the health check API."""

    def test_health_check(self):
        url = reverse("health-check")
        client = APIClient()
        res = client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
