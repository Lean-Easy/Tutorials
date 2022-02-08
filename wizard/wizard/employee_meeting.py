# -*- coding: utf-8 -*-

from odoo import fields, models


class EmployeeMeeting(models.TransientModel):
    _name = "employee.meeting"

    employee_id = fields.Many2one('employee.employee')
    note = fields.Text(string="Meeting Notes", required=True)

    def add_meeting_note(self):
        self.employee_id.note = self.note
