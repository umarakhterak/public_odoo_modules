from odoo import http, fields
from odoo.http import request
from datetime import timedelta


class EmployeePanel(http.Controller):
    @http.route('/product/product_panel', auth='user', type='json')
    def get_panel_data(self):
        today = fields.Date.today()
        future_date = today + timedelta(days=7)

        # Accessing the model via request.env
        total_products = request.env['product.template'].sudo().search_count([
            ('expiry_date', '>=', today),
            ('expiry_date', '<=', future_date),
        ])

        vals = {'total_products': total_products}
        html = request.env['ir.ui.view']._render_template(
            'product_auto_expiry_alert.product_panel', vals
        )
        return {'html': html}

