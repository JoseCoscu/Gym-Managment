from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'product.template'

    #this field is duplicate... the product template model aready have a field for the weight of products
    weight = fields.Float(string='Weight')
    size = fields.Selection(selection=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('big', 'Big')],
        string="Weights Size", compute='compute_size')

    @api.onchange('weight')
    def compute_size(self):
        for record in self:
            if record.weight > 25:
                record.size = 'big'
                return
            if record.weight >= 10:
                record.size = 'medium'
                return
            if record.weight < 10:
                record.size = 'small'
                return
