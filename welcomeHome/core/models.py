from django.db import models
from tinymce import models as tinymce_models


class Country(models.Model):
    """Country object."""

    country = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    countryDescription = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    language = tinymce_models.HTMLField(blank=True, default='', null=True)
    specialConditionsForUkrainianWomen = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    medicalInsuranceForNonCitizens = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    medicalInsuranceCoverageForPregnancyAndChildbirth = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    organizationOfPrenatalCare = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    prenatalCareForNonCitizens = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    costOfDelivery = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    organizationOfDelivery = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    naturalBirthOrCesareanSection =\
        tinymce_models.HTMLField(blank=True, default='', null=True)
    citizenshipOfChildByBirth = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    prospectsOfParentsObtainingCitizenship = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    durationOfMaternityLeave = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    preparationCoursesForChildbirth = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    durationOfJobProtectionForMother = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    paymentsDuringPregnancy = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    childBenefits = tinymce_models.HTMLField(blank=True, default='', null=True)
    benefitsForMothersAndChildren = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    breastfeedingSupport = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    postnatalSupportGroups = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    arrangementOfChildCareFacilities = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    mandatoryAgeForKindergarten = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    costOfDaycare = tinymce_models.HTMLField(blank=True, default='', null=True)
    nursery = tinymce_models.HTMLField(blank=True, default='', null=True)
    costOfNursery = tinymce_models.HTMLField(blank=True, default='', null=True)
    mandatorySchoolAge = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    bonusesForHaving23Children = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    conditionsForSingleMothers = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    conditionsForChildrenWithDisabilities = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    referencesToAssociationsFundsForMoms = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    doctorAppointmentBookingAndPhysicianReviews = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    immigrationConditionsResidencePermit = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    referencesToMigrantCommunities = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    psychologicalSupport = \
        tinymce_models.HTMLField(blank=True, default='', null=True)
    additionalUsefulResourcesAndLinks = \
        tinymce_models.HTMLField(blank=True, default='', null=True)

    class Meta:
        verbose_name_plural = "Countries"
