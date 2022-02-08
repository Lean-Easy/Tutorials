# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_salary = fields.Monetary(string="Default Employee Salary", currency_field='currency_id', default_model="employee.employee")
    currency_id = fields.Many2one('res.currency', default=lambda x: x.env.company.currency_id)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        ICPSudo = self.env['ir.config_parameter'].sudo()

        res.update(
            default_salary=ICPSudo.get_param('employee.default_salary', default=20000),
        )

        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()

        ICPSudo = self.env['ir.config_parameter'].sudo()

        ICPSudo.set_param("employee.default_salary", self.default_salary)
