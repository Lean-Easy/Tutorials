# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Employee(models.Model):
    _name = "employee.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']

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

    @api.model
    def create(self, vals):
        res = super(Employee, self).create(vals)

        res.activity_schedule(
            act_type_xmlid='scheduled_activities.employee_take_photo'
        )

        return res
