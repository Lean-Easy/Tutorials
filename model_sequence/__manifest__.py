# -*- coding: utf-8 -*-
{
    'name': 'Model Sequence Example',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'An example of how to create a sequence for a model.',
    'author': "Lean Easy",
    'website': "https://www.leaneasy.co.uk",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',

        'data/ir_sequence.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
