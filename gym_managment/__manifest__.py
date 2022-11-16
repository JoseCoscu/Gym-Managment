# -*- coding: utf-8 -*-
{
    'name': "Gym Managment",

    'summary': """
        Manage Gym""",

    'description': """
        - Base company coding management.\n
        - Management of selection of types of companies.\n
        - Creation of the CENTRAL partner.\n
    """,

    'author': "Jose_Coscu",

    'version': '14.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','product'],

    # always loaded
    'data': [

        'views/res_partner_view.xml',
        'views/product_template.xml',
    ],
}
