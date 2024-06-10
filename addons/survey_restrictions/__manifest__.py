# -*- coding: utf-8 -*-
{
    'name': "Restricciones de encuestas",
    'summary': """
        Allow create multiple picking in purchase order
    """,
    'author': "Elvis Páez",
    'website': "elvispaez18@gmail.com",
    'category': 'Survey',
    'version': '16.0.0.1',
    'depends': ['survey','hr_appraisal_survey'],
    'data': [
        "views/survey_survey_views.xml",
        "views/survey_user_inputs.xml"
    ],
}
