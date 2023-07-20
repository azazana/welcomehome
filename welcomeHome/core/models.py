from django.db import models


class Country(models.Model):
    """Country object."""

    country = models.CharField(max_length=255,null=True)
    code = models.CharField(max_length=255,null=True)
    countryDescription = models.TextField(blank=True, null=True)
    language = models.TextField(max_length=255, blank=True, null=True)
    specialConditionsForUkrainianWomen = models.TextField(max_length=255, blank=True, null=True)
    medicalInsuranceForNonCitizens = models.TextField(max_length=255, blank=True, null=True)
    medicalInsuranceCoverageForPregnancyAndChildbirth = models.TextField(max_length=255, blank=True, null=True)
    organizationOfPrenatalCare = models.TextField(max_length=255, blank=True, null=True)
    prenatalCareForNonCitizens = models.TextField(max_length=255, blank=True, null=True)
    costOfDelivery = models.TextField(max_length=255, blank=True, null=True)
    organizationOfDelivery = models.TextField(max_length=255, blank=True, null=True)
    naturalBirthOrCesareanSection = models.TextField(max_length=255, blank=True, null=True)
    citizenshipOfChildByBirth = models.TextField(max_length=255, blank=True, null=True)
    prospectsOfParentsObtainingCitizenship = models.TextField(max_length=255, blank=True, null=True)
    durationOfMaternityLeave = models.TextField(max_length=255, blank=True, null=True)
    preparationCoursesForChildbirth = models.TextField(max_length=255, blank=True, null=True)
    durationOfJobProtectionForMother = models.TextField(max_length=255, blank=True, null=True)
    paymentsDuringPregnancy = models.TextField(max_length=255, blank=True, null=True)
    childBenefits = models.TextField(max_length=255, blank=True, null=True)
    benefitsForMothersAndChildren = models.TextField(max_length=255, blank=True, null=True)
    breastfeedingSupport = models.TextField(max_length=255, blank=True, null=True)
    postnatalSupportGroups = models.TextField(max_length=255, blank=True, null=True)
    arrangementOfChildCareFacilities = models.TextField(max_length=255, blank=True, null=True)
    mandatoryAgeForKindergarten = models.TextField(max_length=255, blank=True, null=True)
    costOfDaycare = models.TextField(max_length=255, blank=True, null=True)
    nursery = models.TextField(max_length=255, blank=True, null=True)
    costOfNursery = models.TextField(max_length=255, blank=True, null=True)
    mandatorySchoolAge = models.TextField(max_length=255, blank=True, null=True)
    bonusesForHaving23Children = models.TextField(max_length=255, blank=True, null=True)
    conditionsForSingleMothers = models.TextField(max_length=255, blank=True, null=True)
    conditionsForChildrenWithDisabilities = models.TextField(max_length=255, blank=True, null=True)
    referencesToAssociationsFundsForMoms = models.TextField( blank=True, null=True)
    doctorAppointmentBookingAndPhysicianReviews = models.TextField(max_length=255, blank=True, null=True)
    immigrationConditionsResidencePermit = models.TextField(max_length=255, blank=True, null=True)
    referencesToMigrantCommunities = models.TextField(max_length=255, blank=True, null=True)
    psychologicalSupport = models.TextField(max_length=255, blank=True, null=True)
    additionalUsefulResourcesAndLinks = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "Countries"
