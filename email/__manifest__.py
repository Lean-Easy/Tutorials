# -*- coding: utf-8 -*-
{
    'name': 'Email Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create an email template and send an email.',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'data/employee_email_template.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
