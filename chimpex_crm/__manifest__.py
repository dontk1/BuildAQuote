# -*- coding: utf-8 -*-
# © 2018 Intelligenti <http://www.intelligenti.io>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Chimpex CRM',
    'summary': '',
    'description': 'Chimpex CRM',
    'author': 'Intelligenti',
    'category': 'Sales',
    'license': 'AGPL-3',
    'website': 'http://www.intelligenti.io',
    'version': '11.0.0.0.0',
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'crm',
    ],
    'data': ['wizard/crm_lead_wizard_view.xml',
             'views/crm_lead_view.xml', 
            ],
}