# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class surveySurvey(models.Model):
    _inherit = "survey.survey"

    show_only_admin = fields.Boolean(string=_('Mostrar solo para administrador'))
    evalution_employee = fields.Boolean(string=_('Encuesta 360'), default=False)