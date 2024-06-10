# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class ProductTemplate(models.Model):
    _inherit = "product.template"

    delivery_to = fields.Many2one(
        string=_('Entregar a'),
        comodel_name='stock.picking.type',
    )