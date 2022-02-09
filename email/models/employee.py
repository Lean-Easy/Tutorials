# -*- coding: utf-8 -*-

from odoo import fields, models


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
    email = fields.Char(string="Email")

    def raise_salary(self):
        # get raise salary template
        try:
            template_id = self.env.ref('email.email_template_employee', raise_if_not_found=True)
        except ValueError:
            template_id = False

        if not template_id:
            return

        for rec in self:
            if rec.salary >= 35000:
                rec.salary += 1000
            elif rec.salary > 25000:
                rec.salary += 500
            else:
                rec.salary += 300

            display_name = "My Company"
            email_from_email = "test@company.com"
            reply_to_email = "test@company.com"

            email_values = {
                'email_from': f"{display_name} <{email_from_email}>",
                'reply_to': reply_to_email,
                'email_to': rec.email
            }

            template_id.sudo().send_mail(res_id=rec.id, force_send=True, email_values=email_values)
