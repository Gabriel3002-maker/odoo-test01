# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re
import math

class hrSkillHistory(models.Model):
    _name = "hr.skill.history"
    _description = 'Historial de habilidades'

    appraisal_id = fields.Many2one(
        string=_('Valoración'),
        comodel_name='hr.appraisal',
    )
    skill_type_id = fields.Many2one(
        string=_('Tipo de habilidad'),
        comodel_name='hr.skill.type',
    )
    skill_id = fields.Many2one(
        string=_('Habilidad'),
        comodel_name='hr.skill',
    )
    skill_level_id = fields.Many2one(
        string=_('Nivel de habilidad'),
        comodel_name='hr.appraisal',
    )
    level_progress = fields.Integer(string=_('En proceso'))
    date = fields.Date(
        string=_('Fecha'),
        default=fields.Date.context_today,
    )