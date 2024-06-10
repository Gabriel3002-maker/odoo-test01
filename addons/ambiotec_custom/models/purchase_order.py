# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, Command
import json
import re

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def upadte_qty_invoices(self):
        for rec in self:
            if rec.invoice_status != 'invoiced':
                for line in rec.order_line:
                    if line.product_id and line.qty_invoiced != line.product_qty:
                        for invoice in rec.invoice_ids:
                            line_inv = invoice.invoice_line_ids.filtered(lambda x: x.product_id.id == line.product_id.id)
                            line.invoice_lines = [Command.set(line_inv.ids)]
