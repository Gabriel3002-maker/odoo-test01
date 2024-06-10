# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
import json
import re


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    allow_multiple_picking = fields.Boolean(string=_('Permitir multiples recepciones'), default=False)

    def _create_picking(self):
        if self.allow_multiple_picking:
            StockPicking = self.env['stock.picking']
            for order in self.filtered(lambda po: po.state in ('purchase', 'done')):
                if any(product.type in ['product', 'consu'] for product in order.order_line.product_id):
                    order = order.with_company(order.company_id)
                    pickings = order.picking_ids.filtered(lambda x: x.state not in ('done', 'cancel'))
                    if not pickings:
                        dest_ids = order.order_line.mapped('delivery_to')
                        ids = []
                        for dest in dest_ids:
                            res = order._prepare_picking_delivery(dest)
                            picking = StockPicking.with_user(SUPERUSER_ID).create(res)
                            ids.append(picking.id)
                        pickings = StockPicking.search([('id','in',ids)])
                    else:
                        picking = pickings[0]
                    for pick in pickings:
                        moves = order.order_line.filtered(lambda x: x.delivery_to.id == pick.picking_type_id.id)._create_stock_moves(pick)
                        moves = moves.filtered(lambda x: x.state not in ('done', 'cancel'))._action_confirm()
                        seq = 0
                        for move in sorted(moves, key=lambda move: move.date):
                            seq += 5
                            move.sequence = seq
                        moves._action_assign()
                    # Get following pickings (created by push rules) to confirm them as well.
                    forward_pickings = self.env['stock.picking']._get_impacted_pickings(moves)
                    (pickings | forward_pickings).action_confirm()
                    picking.message_post_with_view('mail.message_origin_link',
                        values={'self': picking, 'origin': order},
                        subtype_id=self.env.ref('mail.mt_note').id)
            return True
        else:
            return super(PurchaseOrder, self)._create_picking()


    def _prepare_picking_delivery(self, location):
        if not self.group_id:
            self.group_id = self.group_id.create({
                'name': self.name,
                'partner_id': self.partner_id.id
            })
        if not self.partner_id.property_stock_supplier.id:
            raise UserError(_("You must set a Vendor Location for this partner %s", self.partner_id.name))
        return {
            'picking_type_id': location.id,
            'partner_id': self.partner_id.id,
            'user_id': False,
            'date': self.date_order,
            'origin': self.name,
            'location_dest_id': location.default_location_dest_id.id,
            'location_id': self.partner_id.property_stock_supplier.id,
            'company_id': self.company_id.id,
        }