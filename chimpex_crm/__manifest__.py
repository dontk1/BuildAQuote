# -*- coding: utf-8 -*-
# © 2018 Tosin Komolafe <http://tosinkomolafe.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Chimpex CRM',
    'summary': '',
    'description': 'Chimpex CRM',
    'author': 'Tosin Komolafe',
    'category': 'Sales',
    'license': 'AGPL-3',
    'website': 'https://tosinkomolafe.com',
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