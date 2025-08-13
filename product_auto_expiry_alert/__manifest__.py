{
    "name": "Expiry Product Alert",
    "version": "16.0.0.1",
    "author": "Muhammad Umar",
    'description': """Expiry Product Alert.""",
    "category": "Product",
    "depends": ['product', 'mail'],
    "data": [
        'views/product_template_view.xml',
        'views/product_banner.xml',
        'data/email_template.xml',
        'data/cron_expiry_alert.xml'
    ],
    "installable": True,
    "application": False,
    'license': 'LGPL-3',
}
