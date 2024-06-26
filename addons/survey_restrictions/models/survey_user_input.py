# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class surveyUserInput(models.Model):
    _inherit = "survey.user_input"

    is_appraisal = fields.Boolean(string=_('Es confidencial'), 
                                  related="survey_id.is_appraisal")
    show_only_admin = fields.Boolean(string=_('Mostrar solo para administrador'), 
                                    related="survey_id.show_only_admin")
    show_info = fields.Boolean(string=_('Mostrar información'), compute="_compute_show_info")


    @api.depends('is_appraisal','show_only_admin')
    def _compute_show_info(self):
        for rec in self:
            action = True
            if rec.is_appraisal:
                action = False
            if rec.show_only_admin and not self.user_has_groups('survey_restrictions.group_survey_admin'):
                action = False
            rec.show_info = action