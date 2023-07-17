import pandas as pd
from core.models import Country


def upload_data_from_excel():
    df = pd.read_excel("CountryExample.xlsx")
    Country.objects.all().delete()

    for _, row in df.iterrows():
        info = {'Country': row['Country'],
                'Code': row['Code'],
                'Country2': row['Country2'],
                'Language': row['Language'],
                'specialConditionsForUkrainianWomen': row['SpecialConditionsForUkrainianWomen'],
                "medicalInsuranceForNonCitizens": row['MedicalInsuranceForNonCitizens'],
                'medicalInsuranceCoverageForPregnancyAndChildbirth': row[
                    'MedicalInsuranceCoverageForPregnancyAndChildbirth'],
                'organizationOfPrenatalCare': row['OrganizationOfPrenatalCare'],
                'prenatalCareForNonCitizens': row['PrenatalCareForNonCitizens'],
                'costOfDelivery': row['CostOfDelivery'],
                'organizationOfDelivery': row['OrganizationOfDelivery'],
                'naturalBirthOrCesareanSection': row['NaturalBirthOrCesareanSection'],
                'citizenshipOfChildByBirth': row['CitizenshipOfChildByBirth'],
                'prospectsOfParentsObtainingCitizenship': row['ProspectsOfParentsObtainingCitizenship'],
                'durationOfMaternityLeave': row['DurationOfMaternityLeave'],
                'preparationCoursesForChildbirth': row['PreparationCoursesForChildbirth'],
                'durationOfJobProtectionForMother': row['DurationOfJobProtectionForMother'],
                'paymentsDuringPregnancy': row['PaymentsDuringPregnancy'],
                'childBenefits': row['ChildBenefits'],
                'benefitsForMothersAndChildren': row['BenefitsForMothersAndChildren'],
                'breastfeedingSupport': row['BreastfeedingSupport'],
                'postnatalSupportGroups': row['PostnatalSupportGroups'],
                'arrangementOfChildCareFacilities': row['ArrangementOfChildCareFacilities'],
                'mandatoryAgeForKindergarten': row['MandatoryAgeForKindergarten'],
                'costOfDaycare': row['CostOfDaycare'],
                'nursery': row['Nursery'],
                'costOfNursery': row['CostOfNursery'],
                'mandatorySchoolAge': row['MandatorySchoolAge'],
                'bonusesForHaving23Children': row['BonusesForHaving23Children'],
                'conditionsForSingleMothers': row['ConditionsForSingleMothers'],
                'conditionsForChildrenWithDisabilities': row['ConditionsForChildrenWithDisabilities'],
                'referencesToAssociationsFundsForMoms': row['ReferencesToAssociationsFundsForMoms'],
                'doctorAppointmentBookingAndPhysicianReviews': row['DoctorAppointmentBookingAndPhysicianReviews'],
                'immigrationConditionsResidencePermit': row['ImmigrationConditionsResidencePermit'],
                'referencesToMigrantCommunities': row['ReferencesToMigrantCommunities'],
                'psychologicalSupport': row['PsychologicalSupport'],
                'additionalUsefulResourcesAndLinks': row['AdditionalUsefulResourcesAndLinks'],
                }
        new_country = Country.objects.create(**dict)
        new_country.save()




upload_data_from_excel()
