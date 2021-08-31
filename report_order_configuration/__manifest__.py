# -*- coding: utf-8 -*-
# Developed By Haresh Chavda <chavdaharesh69@gmail.com>
# Developed by Kiran Kantesariya <kiran.backup0412@gmail.com>
# Original concept by Ossi Mäntylahti <ossiman@gmail.com>

{
	'name': 'report_order_configuration',
    'summary': """
     Odoo PDF order forms order sort""",

    'author': "Terra Colligo",
    'website': "https://www.terracolligo.com",

    'category': 'Reporting',
    "version" : "13.0.0.1",
    "sequence": 1,	
	'depends': ['sale', 'purchase', 'account'],
	'author': 'Terra Colligo',
	'support': 'terracolligo@terracolligo.com',
	"data": [
		'views/order_view.xml',
		'views/purchase_order_view.xml',
		'views/delivery_order_view.xml',
	],
	'images': [],
	"auto_install": False,
	"installable": True,
}
