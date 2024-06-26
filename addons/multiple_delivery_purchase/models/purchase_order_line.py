# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    allow_multiple_picking = fields.Boolean(string=_('Permitir multiples recepciones'),
                                            related="order_id.allow_multiple_picking")
    delivery_to = fields.Many2one(
        string=_('Entregar a'),
        comodel_name='stock.picking.type',
    )

    @api.onchange('product_id')
    def _onchange_field(self):
        if self.product_id:
            if self.product_id.product_tmpl_id:
                self.delivery_to = self.product_id.product_tmpl_id.delivery_to.id

    def _create_stock_moves(self, picking):
        values = []
        for line in self.filtered(lambda l: not l.display_type):
            for val in line._prepare_stock_moves(picking):
                values.append(val)
            line.move_dest_ids.created_purchase_line_id = False
        return self.env['stock.move'].create(values)