# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class surveyQuestion(models.Model):
    _inherit = "survey.question"

    skill_id = fields.Many2one(
        string=_('Habilidad'),
        comodel_name='hr.skill',
    )
    evalution_employee = fields.Boolean(string=_('Encuesta 360'),
        related="survey_id.evalution_employee")