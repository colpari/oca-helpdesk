# -*- coding: utf-8 -*-
{
    'name': "colpari OCA Helpdesk Extension",

    'summary': """
        Customized the OCA Helpdesk Management App.""",

    'description': """
        
    """,

    'author': "colpari GmbH",
    'website': "http://www.colpari.cx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'After-Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk_mgmt'],
    'auto_install': True,

    # always loaded
    'data': [
        'views/change_ticket_views.xml',
    ],
}
