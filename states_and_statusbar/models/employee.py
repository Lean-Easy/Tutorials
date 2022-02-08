# -*- coding: utf-8 -*-

from odoo import fields, models


class Employee(models.Model):
    _name = "employee.employee"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('verified', 'Verified')
    ], required=True, default='draft')

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

    def verify(self):
        for rec in self:
            rec.state = 'verified'
