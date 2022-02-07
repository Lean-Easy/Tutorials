# -*- coding: utf-8 -*-
{
    'name': 'Inherit Model Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to inherit a model in Odoo.',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base', 'first_module'],
    'data': [
        'views/employee_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
