# -*- coding: utf-8 -*-
{
    'name': 'Notification Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of a how to create notifications in Odoo.',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
