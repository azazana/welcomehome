# Generated by Django 4.2.2 on 2023-10-06 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_country_additionalusefulresourcesandlinks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialConditionsOfDepositForUkrainians', models.CharField(choices=[('безкоштовно', 'безкоштовно'), ('ні', 'ні')], max_length=11)),
                ('citizenshipByBirth', models.BooleanField()),
                ('costOfBirthInStateClinic', models.CharField(choices=[('безкоштовно', 'безкоштовно з державним страхуванням')], max_length=36)),
                ('minimumDurationOfPaidMaternityLeave', models.CharField(choices=[('0', '0'), ('0 - 5', '0 - 5'), ('5 - 10', '5 - 10'), ('10 - 15', '10 - 15'), ('15 - 20', '15 - 20'), ('20 - 30', '20 - 30'), ('30 - 40', '30 - 40'), ('40 - 50', '40 - 50'), ('50 - 65', '50 - 65'), ('65+', '65+')], max_length=9)),
                ('freeKindergarten', models.BooleanField()),
                ('hoursPerWeekChildrenFreePreschoolEducation', models.CharField(choices=[('n/a', 'n/a'), ('0 - 10', '0 - 10'), ('10 - 15', '10 - 15'), ('15 - 20', '15 - 20'), ('20 - 30', '20 - 30'), ('30 - 45', '30 - 45')], max_length=11)),
                ('ageFreePreschoolEducation', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('не мають', 'не мають'), ('n/a', 'n/a')], max_length=11)),
                ('costOfChildcareFromUSDPerMonth', models.IntegerField(null=True)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
        ),
    ]