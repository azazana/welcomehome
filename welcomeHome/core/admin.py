from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.CountryFilters)
