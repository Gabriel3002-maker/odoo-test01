# -*- coding: utf-8 -*-
{
    'name': "Multiple delivery purchase",
    'summary': """
        Allow create multiple picking in purchase order
    """,
    'author': "Elvis Páez",
    'website': "elvispaez18@gmail.com",
    'category': 'Survey',
    'version': '16.0.0.1',
    'depends': ['purchase','purchase_stock'],
    'data': [
        "views/purchase_order.xml",
        "views/product_template.xml",
    ],
}
