# Generated by Django 4.2.2 on 2023-07-29 04:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_country_additionalusefulresourcesandlinks_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='additionalUsefulResourcesAndLinks',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='arrangementOfChildCareFacilities',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='benefitsForMothersAndChildren',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='bonusesForHaving23Children',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='breastfeedingSupport',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='childBenefits',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='citizenshipOfChildByBirth',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='conditionsForChildrenWithDisabilities',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='conditionsForSingleMothers',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='costOfDaycare',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='costOfDelivery',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='costOfNursery',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='countryDescription',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='doctorAppointmentBookingAndPhysicianReviews',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='durationOfJobProtectionForMother',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='durationOfMaternityLeave',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='immigrationConditionsResidencePermit',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='language',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='mandatoryAgeForKindergarten',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='mandatorySchoolAge',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='medicalInsuranceCoverageForPregnancyAndChildbirth',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='medicalInsuranceForNonCitizens',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='naturalBirthOrCesareanSection',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='nursery',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='organizationOfDelivery',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='organizationOfPrenatalCare',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='paymentsDuringPregnancy',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='postnatalSupportGroups',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='prenatalCareForNonCitizens',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='preparationCoursesForChildbirth',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='prospectsOfParentsObtainingCitizenship',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='psychologicalSupport',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='referencesToAssociationsFundsForMoms',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='referencesToMigrantCommunities',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='specialConditionsForUkrainianWomen',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
    ]
