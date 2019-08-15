from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProductStatus(models.Model):
    _name = 'product.status'

    name = fields.Char('Product Status', required=True, )

class ProductProduct(models.Model):
    _inherit = 'product.template'

    product_status_id = fields.Many2one('product.status', 'Product Status', ondelete='cascade')                                                                                                                                                                                
