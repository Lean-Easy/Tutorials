# -*- coding: utf-8 -*-

from odoo import fields, models


class Employee(models.Model):
    _inherit = "employee.employee"

    email = fields.Char(string="Email")
    mobile = fields.Char(string="Mobile")
