# -*- coding: utf-8 -*-
{
    'name': 'Security Groups Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create security groups',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/employee_security.xml',
        'security/ir.model.access.csv',

        'views/employee_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
