# -*- coding: utf-8 -*-
{
    'name': "vit_inherit_hr_department",

    'summary': """
        Add Analytic Account on Hr Department""",

    'description': """
        Add Analytic Account on Hr Department
    """,

    'author': "yusupnk14@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}