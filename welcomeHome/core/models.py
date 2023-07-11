from django.db import models


class Country(models.Model):
    """Country object."""

    country = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    countryDescription = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    specialConditionsForUkrainianWomen = models.CharField(max_length=255, blank=True)
    medicalInsuranceForNonCitizens = models.CharField(max_length=255, blank=True)
    medicalInsuranceCoverageForPregnancyAndChildbirth = models.CharField(max_length=255, blank=True)
    organizationOfPrenatalCare = models.CharField(max_length=255, blank=True)
    prenatalCareForNonCitizens = models.CharField(max_length=255, blank=True)
    costOfDelivery = models.CharField(max_length=255, blank=True)
    organizationOfDelivery = models.CharField(max_length=255, blank=True)
    naturalBirthOrCesareanSection = models.CharField(max_length=255, blank=True)
    citizenshipOfChildByBirth = models.CharField(max_length=255, blank=True)
    prospectsOfParentsObtainingCitizenship = models.CharField(max_length=255, blank=True)
    durationOfMaternityLeave = models.CharField(max_length=255, blank=True)
    preparationCoursesForChildbirth = models.CharField(max_length=255, blank=True)
    durationOfJobProtectionForMother = models.CharField(max_length=255, blank=True)
    paymentsDuringPregnancy = models.CharField(max_length=255, blank=True)
    childBenefits = models.CharField(max_length=255, blank=True)
    benefitsForMothersAndChildren = models.CharField(max_length=255, blank=True)
    breastfeedingSupport = models.CharField(max_length=255, blank=True)
    postnatalSupportGroups = models.CharField(max_length=255, blank=True)
    arrangementOfChildCareFacilities = models.CharField(max_length=255, blank=True)
    mandatoryAgeForKindergarten = models.CharField(max_length=255, blank=True)
    costOfDaycare = models.CharField(max_length=255, blank=True)
    nursery = models.CharField(max_length=255, blank=True)
    costOfNursery = models.CharField(max_length=255, blank=True)
    mandatorySchoolAge = models.CharField(max_length=255, blank=True)
    bonusesForHaving23Children = models.CharField(max_length=255, blank=True)
    conditionsForSingleMothers = models.CharField(max_length=255, blank=True)
    conditionsForChildrenWithDisabilities = models.CharField(max_length=255, blank=True)
    referencesToAssociationsFundsForMoms = models.CharField(max_length=255, blank=True)
    doctorAppointmentBookingAndPhysicianReviews = models.CharField(max_length=255, blank=True)
    immigrationConditionsResidencePermit = models.CharField(max_length=255, blank=True)
    referencesToMigrantCommunities = models.CharField(max_length=255, blank=True)
    psychologicalSupport = models.CharField(max_length=255, blank=True)
    additionalUsefulResourcesAndLinks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "Countries"
