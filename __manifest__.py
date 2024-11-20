# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Sale_extended',
    'version': '1.3',
    'category': 'sale_extended/sale_extended',
    'summary': 'Sale_extended internal machinery',

    'depends': ['base'],

    'data': ['security/sale_group.xml',
            'security/ir.model.access.csv',
             'data/ir_cron.xml',
             'report/ir_actions_report.xml',
             'report/sale_order_report.xml',
            'wizard/invoice_wizard_views.xml',
             'data/ir_sequence_data.xml',
             'views/sale_extended_views.xml',
             'views/invoice_views.xml',
             'views/menu.xml'

             ],

    'demo': [],

    'installable': True,
    'assets': {

    },
    'license': 'LGPL-3',

}
