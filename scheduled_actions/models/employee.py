# -*- coding: utf-8 -*-

from odoo import fields, models


class Employee(models.Model):
    _name = "employee.employee"

    forename = fields.Char(string="Forename")
    surname = fields.Char(string="Surname")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        string="Gender"
    )
    currency_id = fields.Many2one('res.currency', default=lambda x: x.env.company.currency_id) # for salary
    salary = fields.Monetary(string="Salary", currency_field='currency_id')
    photo = fields.Image(string="Photo")
    nationality = fields.Many2one('res.country', string="Nationality")

    def _update_salary_quarterly(self):
        """
        Example of cron job function:
        Updates employee salary quarterly
        """
        employees = self.env['employee.employee'].sudo().search([])

        for rec in employees:
            rec.salary += 500
