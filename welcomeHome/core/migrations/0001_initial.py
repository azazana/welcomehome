# Generated by Django 4.2.2 on 2023-07-28 21:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, null=True)),
                ('country_ru', models.CharField(max_length=255, null=True)),
                ('country_uk', models.CharField(max_length=255, null=True)),
                ('code', models.CharField(max_length=255, null=True)),
                ('countryDescription', tinymce.models.HTMLField(blank=True, default='')),
                ('countryDescription_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('countryDescription_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('language', tinymce.models.HTMLField(blank=True, default='')),
                ('language_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('language_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('specialConditionsForUkrainianWomen', tinymce.models.HTMLField(blank=True, default='')),
                ('specialConditionsForUkrainianWomen_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('specialConditionsForUkrainianWomen_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('medicalInsuranceForNonCitizens', tinymce.models.HTMLField(blank=True, default='')),
                ('medicalInsuranceForNonCitizens_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('medicalInsuranceForNonCitizens_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('medicalInsuranceCoverageForPregnancyAndChildbirth', tinymce.models.HTMLField(blank=True, default='')),
                ('medicalInsuranceCoverageForPregnancyAndChildbirth_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('medicalInsuranceCoverageForPregnancyAndChildbirth_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('organizationOfPrenatalCare', tinymce.models.HTMLField(blank=True, default='')),
                ('organizationOfPrenatalCare_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('organizationOfPrenatalCare_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('prenatalCareForNonCitizens', tinymce.models.HTMLField(blank=True, default='')),
                ('prenatalCareForNonCitizens_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('prenatalCareForNonCitizens_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('costOfDelivery', tinymce.models.HTMLField(blank=True, default='')),
                ('costOfDelivery_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('costOfDelivery_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('organizationOfDelivery', tinymce.models.HTMLField(blank=True, default='')),
                ('organizationOfDelivery_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('organizationOfDelivery_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('naturalBirthOrCesareanSection', tinymce.models.HTMLField(blank=True, default='')),
                ('naturalBirthOrCesareanSection_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('naturalBirthOrCesareanSection_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('citizenshipOfChildByBirth', tinymce.models.HTMLField(blank=True, default='')),
                ('citizenshipOfChildByBirth_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('citizenshipOfChildByBirth_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('prospectsOfParentsObtainingCitizenship', tinymce.models.HTMLField(blank=True, default='')),
                ('prospectsOfParentsObtainingCitizenship_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('prospectsOfParentsObtainingCitizenship_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('durationOfMaternityLeave', tinymce.models.HTMLField(blank=True, default='')),
                ('durationOfMaternityLeave_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('durationOfMaternityLeave_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('preparationCoursesForChildbirth', tinymce.models.HTMLField(blank=True, default='')),
                ('preparationCoursesForChildbirth_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('preparationCoursesForChildbirth_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('durationOfJobProtectionForMother', tinymce.models.HTMLField(blank=True, default='')),
                ('durationOfJobProtectionForMother_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('durationOfJobProtectionForMother_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('paymentsDuringPregnancy', tinymce.models.HTMLField(blank=True, default='')),
                ('paymentsDuringPregnancy_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('paymentsDuringPregnancy_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('childBenefits', tinymce.models.HTMLField(blank=True, default='')),
                ('childBenefits_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('childBenefits_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('benefitsForMothersAndChildren', tinymce.models.HTMLField(blank=True, default='')),
                ('benefitsForMothersAndChildren_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('benefitsForMothersAndChildren_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('breastfeedingSupport', tinymce.models.HTMLField(blank=True, default='')),
                ('breastfeedingSupport_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('breastfeedingSupport_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('postnatalSupportGroups', tinymce.models.HTMLField(blank=True, default='')),
                ('postnatalSupportGroups_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('postnatalSupportGroups_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('arrangementOfChildCareFacilities', tinymce.models.HTMLField(blank=True, default='')),
                ('arrangementOfChildCareFacilities_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('arrangementOfChildCareFacilities_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('mandatoryAgeForKindergarten', tinymce.models.HTMLField(blank=True, default='')),
                ('mandatoryAgeForKindergarten_ru', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('mandatoryAgeForKindergarten_uk', tinymce.models.HTMLField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
