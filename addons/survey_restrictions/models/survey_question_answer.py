# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class surveyQuestionAnswer(models.Model):
    _inherit = "survey.question.answer"

    skill_level_id = fields.Many2one(
        string=_('Puntuación'),
        comodel_name='hr.skill.level',
    )