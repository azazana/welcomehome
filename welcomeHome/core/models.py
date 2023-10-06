from django.db import models
from tinymce import models as tinymce_models
from enum import Enum


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

    class CostOfBirthInStateClinicChoice(Enum):
        CHOICE = "безкоштовно з державним страхуванням"

    class MinimumDurationOfPaidMaternityLeaveChoice(Enum):
        CHOICE1 = "0"
        CHOICE2 = "0 - 5"
        CHOICE3 = "5 - 10"
        CHOICE4 = "10 - 15"
        CHOICE5 = "15 - 20"
        CHOICE6 = "20 - 30"
        CHOICE7 = "30 - 40"
        CHOICE8 = "40 - 50"
        CHOICE9 = "50 - 65"
        CHOICE10 = "65 + "

    class SpecialConditionsOfDepositForUkrainiansChoice(Enum):
        CHOICE = "безкоштовно"
        CHOICE1 = "ні"

    class HoursPerWeekChildrenFreePreschoolEducationChoice(Enum):
        CHOICE1 = "n/a"
        CHOICE2 = "0 - 10"
        CHOICE3 = "10 - 15"
        CHOICE4 = "15 - 20"
        CHOICE5 = "20 - 30"
        CHOICE6 = "30 - 45"

    class TheAgeFreePreschoolEducationChoice(Enum):
        CHOICE1 = "0"
        CHOICE2 = "1"
        CHOICE3 = "2"
        CHOICE4 = "3"
        CHOICE5 = "4"
        CHOICE6 = "5"
        CHOICE7 = "6"
        CHOICE8 = "не мають"
        CHOICE9 = "n/a"

    def _getListOfChoice(self, nameOfClass):
        return [(choice.value, choice.key) for choice in nameOfClass]

    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    specialConditionsOfDepositForUkrainians = models.CharField(max_length=11,
                                                               choices=_getListOfChoice(
                                                                   SpecialConditionsOfDepositForUkrainiansChoice
                                                               ),
                                                               )
    citizenshipByBirth = models.BooleanField()
    costOfChildBirthInStateClinic = models.CharField(max_length=36, choices=_getListOfChoice(
        CostOfBirthInStateClinicChoice
    ))
    minimumDurationOfPaidMaternityLeave = models.CharField(max_length=9,
                                                           choices=_getListOfChoice(
                                                               MinimumDurationOfPaidMaternityLeaveChoice,
                                                           ))
    freeKindergarten = models.BooleanField()
    hoursPerWeekChildrenFreePreschoolEducation = models.CharField(max_length=11,
                                                                  choices=_getListOfChoice(
                                                                      HoursPerWeekChildrenFreePreschoolEducationChoice))
    ageFreePreschoolEducation = models.CharField(max_length=11,
                                                      choices=_getListOfChoice(TheAgeFreePreschoolEducationChoice
                                                                               ))
    costOfChildcareFromUSDPerMonth=models.IntegerField()
    def __str__(self):
        return self.country.name
