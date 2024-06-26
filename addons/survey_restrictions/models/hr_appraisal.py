# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, Command
import json
import re
import math

MULTIPLOS = [20, 40, 60, 80, 100]
class hrAppraisal(models.Model):
    _inherit = "hr.appraisal"

    skill_history_id = fields.One2many(
        string=_('Historial de habilidades'),
        comodel_name='hr.skill.history',
        inverse_name='appraisal_id',
    )
    # hr_employee_ids = fields.Many2many(
    #     string=_('hr_employee_ids'),
    #     comodel_name='hr.employee',
    #     compute="_compute_hr_employee_ids",
    #     store=True
    # )

    # @api.depends('survey_ids.user_input_ids')
    # def _compute_hr_employee_ids(self):
    #     for rec in self:
    #         domain = []
    #         inputs = self.env['survey.user_input'].search([
    #             ('appraisal_id','=',rec.id),
    #             ('state','=','done')
    #         ])
    #         if inputs:
    #             domain = inputs.mapped('partner_id').mapped('employee_ids')
    #         rec.hr_employee_ids = domain

    def redondear_a_multiplo(self, numero, multiplo):
       return round(min(multiplo, key=lambda x: abs(x - numero)))


    def generate_skill_info(self):
        for rec in self:
            inputs = self.env['survey.user_input'].search([
                ('appraisal_id','=',rec.id),
                ('state','=','done')
            ])
            questions_with_skills = inputs.user_input_line_ids.mapped('question_id').filtered(lambda x: x.skill_id)
            if questions_with_skills:
                data_history = []
                for h_skill in rec.skill_ids:
                    data_history.append(Command.create({
                        'date': h_skill.create_date.date(),
                        'appraisal_id': rec.id,
                        'skill_type_id': h_skill.skill_type_id.id,
                        'skill_id': h_skill.skill_id.id,
                        # 'skill_level_id': h_skill.skill_level_id.id,
                        'level_progress': h_skill.level_progress,
                    }))
                rec.skill_history_id = data_history
                rec.skill_ids.unlink()
            for question in questions_with_skills:
                amount = 0
                skill_id = False
                answers = self.env['survey.user_input.line'].search([
                    ('survey_id','=',question.survey_id.id),
                    ('question_id','=',question.id),
                    ('user_input_id.appraisal_id','=',rec.id)
                ])
                for ans in answers:
                    if ans.suggested_answer_id.skill_level_id:
                        skill_id = ans.question_id.skill_id.id
                    amount+= ans.suggested_answer_id.skill_level_id.level_progress
                total_amount = amount/len(answers)
                multiplo = self.redondear_a_multiplo(total_amount, MULTIPLOS)
                level_skill = self.env['hr.skill.level'].search([
                    ('level_progress','=',multiplo)
                ],limit=1)
                if level_skill and skill_id:
                    data = {
                        'skill_id':skill_id,
                        'skill_level_id':level_skill.id,
                        'appraisal_id':rec.id,
                    }
                    self.env['hr.appraisal.skill'].sudo().create(data)

