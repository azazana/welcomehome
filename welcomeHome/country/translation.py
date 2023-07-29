from modeltranslation.translator import register, TranslationOptions
from core.models import Country


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    """
    Class for translation Countries.
    """

    fields = (
        'country',
        'countryDescription',
        'language',
        'specialConditionsForUkrainianWomen',
        'medicalInsuranceForNonCitizens',
        'medicalInsuranceCoverageForPregnancyAndChildbirth',
        'organizationOfPrenatalCare',
        'prenatalCareForNonCitizens',
        'costOfDelivery',
        'organizationOfDelivery',
        'naturalBirthOrCesareanSection',
        'citizenshipOfChildByBirth',
        'prospectsOfParentsObtainingCitizenship',
        'durationOfMaternityLeave',
        'preparationCoursesForChildbirth',
        'durationOfJobProtectionForMother',
        'paymentsDuringPregnancy',
        'childBenefits',
        'benefitsForMothersAndChildren',
        'breastfeedingSupport',
        'postnatalSupportGroups',
        'arrangementOfChildCareFacilities',
        'mandatoryAgeForKindergarten',
        'costOfDaycare',
        'nursery',
        'costOfNursery',
        'mandatorySchoolAge',
        'bonusesForHaving23Children',
        'conditionsForSingleMothers',
        'conditionsForChildrenWithDisabilities',
        'referencesToAssociationsFundsForMoms',
        'doctorAppointmentBookingAndPhysicianReviews',
        'immigrationConditionsResidencePermit',
        'referencesToMigrantCommunities',
        'psychologicalSupport',
        'additionalUsefulResourcesAndLinks'
    )
