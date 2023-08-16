# Generated by Django 4.2.2 on 2023-07-29 04:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='additionalUsefulResourcesAndLinks',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='bonusesForHaving23Children',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='conditionsForChildrenWithDisabilities',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='conditionsForSingleMothers',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='costOfDaycare',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='costOfNursery',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='doctorAppointmentBookingAndPhysicianReviews',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='immigrationConditionsResidencePermit',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='mandatorySchoolAge',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='nursery',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='psychologicalSupport',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='referencesToAssociationsFundsForMoms',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='country',
            name='referencesToMigrantCommunities',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]