import mysql.connector
import pandas as pd
from django.conf import settings

import os
import django
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'welcomeHome.settings')
django.setup()


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

    excel_file = 'path/to/your/excel_file.xlsx'
    df = pd.read_excel(excel_file)

    # Очистка таблицы перед загрузкой новых данных
    cursor.execute('DELETE FROM Country')

    # Загрузка данных в базу данных MySQL
    for _, row in df.iterrows():
        query = """
        INSERT INTO kamal_kays (country, code, country2, language, special_conditions_for_ukrainian_women, medical_insurance_for_non_citizens, medical_insurance_coverage_for_pregnancy_and_child_birth, organization_of_prenatal_care, prenatal_care_for_non_citizens, cost_of_delivery, organization_of_delivery, natural_birth_or_cesarean_section, citizenship_of_child_by_birth, prospects_of_parents_obtaining_citizenship, duration_of_maternity_leave, preparation_courses_for_childbirth, duration_of_job_protection_for_mother, payments_during_pregnancy, child_benefits, benefits_for_mothers_and_children, breastfeeding_support, postnatal_support_groups, arrangement_of_child_care_facilities, mandatory_age_for_kindergarten, cost_of_daycare, nursery, cost_of_nursery, mandatory_school_age, bonuses_for_having_23_children, conditions_for_single_mothers, conditions_for_children_with_disabilities, references_to_associations_funds_for_moms, doctor_appointment_booking_and_physician_reviews, immigration_conditions_residence_permit, references_to_migrant_communities, psychological_support, additional_useful_resources_and_links)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            row['COUNTRY'], row['CODE'], row['COUNTRY_2'], row['LANGUAGE'],
            row['SPECIAL_CONDITIONS_FOR_UKRAINIAN_WOMEN'], row['MEDICAL_INSURANCE_FOR_NON_CITIZENS'],
            row['MEDICAL_INSURANCE_COVERAGE_FOR_PREGNANCY_AND_CHILD_BIRTH'], row['ORGANIZATION_OF_PRENATAL_CARE'],
            row['VEDENNIA_VAHITNOSTI'], row['VARTIST_POLOGIV'], row['ORGANIZATION_OF_DELIVERY'],
            row['PRYRODNI_POLOHY_CHY_KESARIV_ROZTYN'], row['HROMADIANSTVO_DYTINY_ZA_NARODZENNYAM'],
            row['PERSPEKTYVA_OTRYMANNYA_HROMADIANSTVA_BATKAMY'], row['TRYVALIST_DEKRETNOYI_VIDPOUSTKY'],
            row['KURSY_PIDHOTOVKY_DO_POLOHIV'], row['TRYVALIST_ZBEREZHENNYA_ROBOCHOHO_MISTSYA'],
            row['VIPLATY_PO_VAHITNOSTI'], row['VIPLATY_NA_DYTINU'], row['LHOTY_DLYA_MATERIV_DITI'], row['PIDTRYMKA_GV'],
            row['GRUPY_PIDTRYMKY_PISLYA_POLOHIV'], row['YAK_VLASHTOVANI_DYTYACHI_SADKY'],
            row['YAKOHO_VIKU_OBOVYAZKOVI_DYTYACHYI_SADOK'], row['VARTIST_DYTYACHYKH_SADKIV'], row['YASLA'],
            row['VARTIST_YASEL'], row['Z_YAKOHO_VIKU_OBOVYAZKOVA_SHKOLA'], row['BONUSY_NA_2_3_DYTINU'],
            row['UMOVY_DLYA_MATERIV_ODYNACHOK'], row['UMOVY_DLYA_DITEY_Z_INVALIDNISTYU'],
            row['POSYLANNYA_NA_ASOTSIATSII_FONDI_DLYA_MAM'], row['POSYLANNYA_NA_ZAPYS_DO_LIKARYA_I_PEREHLAD_LIKARIV'],
            row['EMIHRAATSIYNI_UMOVY'], row['POSYLANNYA_NA_SPILNOTY_MIHRAANTIV'], row['PSYKHOLIHOCHNA_PIDTRYMKA'],
            row['DODATKOVI_KORYSNI_RESURSY_I_POSYLANNYA']
        )

        cursor.execute(query, values)

    # Сохраняем изменения в базе данных
    cursor.commit()

    cnx.close()


upload_data_from_excel()
