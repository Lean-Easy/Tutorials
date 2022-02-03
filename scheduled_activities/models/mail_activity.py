from odoo import fields, models


class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

    category = fields.Selection(selection_add=[
        ('employee_take_photo', 'Please take a photo for the employee')
    ])
