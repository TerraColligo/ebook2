# -*- coding: utf-8 -*-
{
    'name': "eBook Library",

    'summary': """
        Odoo eBook Library Add-on""",

    'description': """
        publish eBooks on the Odoo platform.
    """,

    'author': "Clouden Oy",
    'website': "https://clouden.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # Fixed version syntax. Odoo add-ons versions scheme must be major odoo version.x.x.x for Odoo to detect changes in modules and apply updates. In this case 13.x.x.x.
    'category': 'Website',
    'version': '13.0.0.8',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'website', 'website_form'],

    # always loaded; these need to be in a specific order
    'data': [
        # Security
        'security/groups.xml',
        'security/ir.model.access.csv',
        # Misc?
        'data/sites.xml',
        # Reports
        # Models
        'views/ebook_views.xml',
        # Menu
        'views/menu_actions.xml',
        'views/menu_items.xml',
        # Form actions
        'views/form_actions.xml',
        # Web
        'views/web/ebooks.xml',
        # Snippets https://www.youtube.com/watch?v=mA4WECek70w
        #'views/snippets/ebook_snippets.xml',
        # Email
        'views/email/ebook_download_email.xml',
    ],
    'css': [
        'static/src/css/ebooks-library.css',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,

    # PIP requirements - install with pip3 install typing-extensions
    'external_dependencies': {
        'python': ['typing-extensions'],
    },
}
