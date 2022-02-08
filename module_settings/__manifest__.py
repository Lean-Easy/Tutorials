# -*- coding: utf-8 -*-
{
    'name': 'Module Settings Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create module settings.',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'views/res_config_settings.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
