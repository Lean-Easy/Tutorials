# -*- coding: utf-8 -*-
{
    'name': 'Scheduled Actions Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create scheduled actions in Odoo',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'data/ir_cron.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
