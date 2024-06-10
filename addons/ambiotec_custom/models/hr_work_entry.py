# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
import re


class hrWorkEntry(models.Model):
    _inherit = "hr.work.entry"

    @api.depends('work_entry_type_id', 'employee_id')
    def _compute_name(self):
        for work_entry in self:
            if not work_entry.employee_id:
                work_entry.name = _('Undefined')
            elif self.user_has_groups('hr_payroll.group_hr_payroll_manager'):
                work_entry.name = "%s: %s" % (work_entry.work_entry_type_id.name or _('Undefined Type'), work_entry.employee_id.name)
            else:
                work_entry.name = "Ausencia: %s" % (work_entry.employee_id.name)

    # @api.depends_context('uid')
    # def _compute_name(self):
    #     res = super(hrWorkEntry, self)._compute_name()
    #     print('#### ENTOR ####')
    #     for rec in self:
    #         if self.user_has_groups('hr_payroll.group_hr_payroll_manager'):
    #             print('#### 1 ###')
    #             rec.name = "%s: %s" % (rec.work_entry_type_id.name or _('Undefined Type'), rec.employee_id.name)
    #         else:
    #             print('#### 2 ###')
    #             print(rec.name)
    #             rec.name = "Ausencia: %s" % (rec.employee_id.name)
    #             print(rec.name)
    #     return res
