# -*- coding: utf-8 -*-
{
    'name': 'Modern Save and Discard Buttons',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Show clear Save and Discard buttons on Odoo form views',
    'description': """
Modern Save and Discard Buttons
===============================
Replace the small icon-only form save and discard controls with clear labeled buttons.

Features:
- Clear Save and Discard buttons in the form control panel
- Consistent styling for form footer save and discard buttons
- Works across standard Odoo form views
- Preserves Odoo keyboard shortcuts: S for Save and J for Discard
- Uses Odoo core web templates only
- No configuration needed
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/modules/browse?repo_maintainer_id=512936',
    'license': 'GPL-3',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'sm_save_discard_buttons/static/src/scss/save_discard_buttons.scss',
            'sm_save_discard_buttons/static/src/xml/save_discard_buttons.xml',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
