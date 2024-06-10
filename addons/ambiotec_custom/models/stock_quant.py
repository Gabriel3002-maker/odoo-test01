# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class stockQuant(models.Model):
    _inherit = "stock.quant"

    inventory_quantity_auto_apply = fields.Float(groups='base.group_user')