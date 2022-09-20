# -*- coding: utf-8 -*-
{
    'name': 'Print Pricelist Report in PDF',
    'summary': "Hide Cost / Sale Price",

    'author': "TopERP Technology Solution Limited, Linh Nguyen",
    'website': "https://toperp.vn/addons/print-pricelist",

    'category': 'Pricelist',
    'version': '1.0',
    'depends': ['web', 'product'],
    "data": [
        'reports/report.xml',
        'reports/report_template.xml',
    ],

    'images': ['static/description/icon.png'],

    'license ': 'LGPL-3',

    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    # 'price': '4.99',
    'currency': 'USD',
}
