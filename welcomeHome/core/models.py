from django.db import models
from tinymce import models as tinymce_models
from enum import Enum
from django.utils.translation import gettext_lazy as _


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
    naturalBirthOrCesareanSection = \
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
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.country}'


class CountryFilters(models.Model):
    """Filters for country."""

    COST_CHOICE = [(_("безкоштовно"), _(
        "безкоштовно з державним страхуванням"
    ))]

    MINIMUM_DURATION_CHOICES = (
        ("0", "0"),
        ("0 - 5", "0 - 5"),
        ("5 - 10", "5 - 10"),
        ("10 - 15", "10 - 15"),
        ("15 - 20", "15 - 20"),
        ("20 - 30", "20 - 30"),
        ("30 - 40", "30 - 40"),
        ("40 - 50", "40 - 50"),
        ("50 - 65", "50 - 65"),
        ("65+", "65+")
    )

    SPECIAL_UK_CHOICE = (_("безкоштовно"), _("безкоштовно")), (_("ні"), _("ні"))

    HOURS_PER_WEEK_CHOICES = (
        ("n/a", "n/a"),
        ("0 - 10", "0 - 10"),
        ("10 - 15", "10 - 15"),
        ("15 - 20", "15 - 20"),
        ("20 - 30", "20 - 30"),
        ("30 - 45", "30 - 45")
    )

    AGE_CHOICES = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        (_("не мають"), _("не мають")),
        ("n/a", "n/a")
    )

    def _getListOfChoice(self, nameOfClass):
        return [(choice.value, choice.key) for choice in nameOfClass]

    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    specialConditionsOfDepositForUkrainians = models.CharField(max_length=11,
                                                               choices=SPECIAL_UK_CHOICE,
                                                               )
    citizenshipByBirth = models.BooleanField(default=False, blank=False,null=False)
    costOfBirthInStateClinic = models.CharField(max_length=36, choices=COST_CHOICE)
    minimumDurationOfPaidMaternityLeave = models.CharField(max_length=9,
                                                           choices=MINIMUM_DURATION_CHOICES
                                                           )
    freeKindergarten = models.BooleanField(default=False, blank=False,null=False)
    hoursPerWeekChildrenFreePreschoolEducation = models.CharField(max_length=11,
                                                                  choices=HOURS_PER_WEEK_CHOICES)
    ageFreePreschoolEducation = models.CharField(max_length=11,
                                                 choices=AGE_CHOICES
                                                 )
    costOfChildcareFromUSDPerMonth = models.IntegerField(null=True)

    def __str__(self):
        return self.country.country
