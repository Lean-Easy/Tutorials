# -*- coding: utf-8 -*-
{
    'name': 'Simple Report Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of a how to create a simple report in Odoo',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'reports/employee_actions.xml',
        'reports/employee_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
