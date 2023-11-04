import os

import django
import mysql.connector
import pandas as pd
from django.conf import settings
from dotenv import load_dotenv

import certifi
import urllib3

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'welcomeHome.settings')
django.setup()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
url = 'https://typograf.ru/webservice/'


def get_typogram(text):
    if " " not in text:
        return text
    else:
        return urllib3.PoolManager().request(
            'POST',
            url,
            fields={'text': text,
                    'chr': 'UTF-8'}).data.decode('utf8')


def upload_data_from_excel():
    db_config = settings.DATABASES['default']

    # Создание подключения к базе данных MySQL
    cnx = mysql.connector.connect(
        host=db_config['HOST'],
        user=db_config['USER'],
        password=db_config['PASSWORD'],
        database=db_config['NAME'],
    )

    cursor = cnx.cursor()

    excel_file = 'CountryExample.xlsx'
    df = pd.read_excel(excel_file)
    df = df.where(pd.notna(df), None)

    # Очистка таблицы перед загрузкой новых данных
    cursor.execute('DELETE FROM core_country')

    # Загрузка данных в базу данных MySQL
    for _, row in df.iterrows():
        # Assuming you have 37 columns in the core_country table
        query = """
            INSERT INTO core_country (
            country_uk, code, countryDescription_uk, language_uk,
            specialConditionsForUkrainianWomen_uk,
            medicalInsuranceForNonCitizens_uk,
            medicalInsuranceCoverageForPregnancyAndChildbirth_uk,
            organizationOfPrenatalCare_uk, prenatalCareForNonCitizens_uk,
            costOfDelivery_uk,
            organizationOfDelivery_uk, naturalBirthOrCesareanSection_uk,
            citizenshipOfChildByBirth_uk,
            prospectsOfParentsObtainingCitizenship_uk,
            durationOfMaternityLeave_uk, preparationCoursesForChildbirth_uk,
            durationOfJobProtectionForMother_uk, paymentsDuringPregnancy_uk,
            childBenefits_uk, benefitsForMothersAndChildren_uk,
            breastfeedingSupport_uk,
            postnatalSupportGroups_uk, arrangementOfChildCareFacilities_uk,
            mandatoryAgeForKindergarten_uk, costOfDaycare_uk,
            nursery_uk, costOfNursery_uk, mandatorySchoolAge_uk,
            bonusesForHaving23Children_uk, conditionsForSingleMothers_uk,
            conditionsForChildrenWithDisabilities_uk,
            referencesToAssociationsFundsForMoms_uk,
            doctorAppointmentBookingAndPhysicianReviews_uk,
            immigrationConditionsResidencePermit_uk,
            referencesToMigrantCommunities_uk, psychologicalSupport_uk,
            additionalUsefulResourcesAndLinks_uk
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Assuming 'row' is a tuple containing data
        # to be inserted into the table
        values = (
            row[0], row[1], row[2], row[3], row[4],
            row[5], row[6], row[7], row[8],
            row[9], row[10], row[11], row[12], row[13],
            row[14], row[15], row[16], row[17],
            row[18], row[19], row[20], row[21],
            row[22], row[23], row[24], row[25], row[26],
            row[27], row[28], row[29], row[30],
            row[31], row[32], row[33], row[34],
            row[35], row[36]
        )
        result = tuple(get_typogram(element) if element is not None else None
                       for element in values)
        # Execute the query using the cursor and values
        cursor.execute(query, result)

        # Сохраняем изменения в базе данных
    cnx.commit()
    cursor.close()
    cnx.close()


upload_data_from_excel()
