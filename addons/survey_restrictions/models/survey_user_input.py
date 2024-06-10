# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class surveyUserInput(models.Model):
    _inherit = "survey.user_input"

    is_appraisal = fields.Boolean(string=_('Es confidencial'), 
                                  related="survey_id.is_appraisal")