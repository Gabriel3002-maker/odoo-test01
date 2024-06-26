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
    'depends': ['survey','hr_appraisal_survey','hr_appraisal_skills'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/survey_survey_views.xml",
        "views/survey_user_inputs.xml",
        "views/hr_appraisal.xml",
        "wizard/appraisal_ask_feedback.xml"
    ],
}
