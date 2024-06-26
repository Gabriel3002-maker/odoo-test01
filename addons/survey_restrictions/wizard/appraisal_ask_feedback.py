# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, Command, _
from odoo.exceptions import UserError
from odoo.tools import html_sanitize, is_html_empty

_logger = logging.getLogger(__name__)


class AppraisalAskFeedback(models.TransientModel):
    _inherit = 'appraisal.ask.feedback'

    domain_employee_ids = fields.Many2many(
        domain_string=_('Dominio de empleados'),
        comodel_name='hr.employee',
        compute="_compute_domain_employee"
    )

    @api.depends('appraisal_id')
    def _compute_domain_employee(self):
        domain = []
        if self.appraisal_id:
            domain = self.env['hr.employee']\
                .search([('id','not in',self.appraisal_id.employee_feedback_ids.ids)]).ids
        self.domain_employee_ids = domain