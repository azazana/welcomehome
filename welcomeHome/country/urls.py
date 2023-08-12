"""
URL mapping for the country api.
"""

from country import views
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("country", views.CountryViewSet)
app_name = "country"

urlpatterns = [
    path("", include(router.urls)),
    path("details/<int:id>", views.details, name="details"),
    path("index/", views.index, name="index"),
]
