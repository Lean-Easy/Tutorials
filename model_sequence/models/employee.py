# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Employee(models.Model):
    _name = "employee.employee"

    name = fields.Char(string="Employee Number", required=True, readonly=True, copy=False, default=_('New'))

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
    def create(self, vals_list):
        if vals_list.get('name', _('New')) == _('New'):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('employee.employee') or _('New')

        return super(Employee, self).create(vals_list)
