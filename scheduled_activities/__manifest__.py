# -*- coding: utf-8 -*-
{
    'name': 'Scheduled Activity Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create scheduled activities in Odoo',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'data/mail_activity.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
