from odoo import models, fields, api
from datetime import timedelta

class ProductExpiryAlert(models.Model):
    _inherit = 'product.template'

    expiry_date = fields.Date(string="Expiry Date")
    expiring_soon = fields.Boolean(string="Expiry Products", compute="_compute_is_expiring_soon", store=True)

    @api.model
    def check_product_expiry(self):
        today = fields.Date.today()
        upcoming = today + timedelta(days=7)
        products = self.search([
            ('expiry_date', '!=', False),
            ('expiry_date', '<=', upcoming),
            ('expiry_date', '>=', today)
        ])
        if products:
            # Send email to inventory team
            template_id = self.env.ref('product_auto_expiry_alert.email_template_product_expiry_alert')
            record = products[0]
            template_id.with_context(expiring_products=products).send_mail(record.id, force_send=True)

            # for product in products:
            #     template_id.send_mail(product.id, force_send=True)

    @api.depends('expiry_date')
    def _compute_is_expiring_soon(self):
        today = fields.Date.today()
        upcoming = today + timedelta(days=7)
        for rec in self:
            rec.expiring_soon = rec.expiry_date and today <= rec.expiry_date <= upcoming