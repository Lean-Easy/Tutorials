# -*- coding: utf-8 -*-

from odoo import fields, models, _


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

    def show_notification_success(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Notification Title'),
                'message': 'Notification message content.',
                'type': 'success',
                'sticky': True,
            },
        }

    def show_notification_warning(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Notification Title'),
                'message': 'Notification message content.',
                'type': 'warning',
                'sticky': True,
            },
        }

    def show_notification_danger(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Notification Title'),
                'message': 'Notification message content.',
                'type': 'danger',
                'sticky': True,
            },
        }

    def show_notification_info(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Notification Title'),
                'message': 'Notification message content.',
                'type': 'info',
                'sticky': True,
            },
        }
