# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_coach = fields.Boolean(string='Is Coach', default=False)
    pupils = fields.One2many('res.partner', inverse_name='parent_id' ,string='Pupils')
    #coach=fields.Many2one('res.partner', inverse='pupils')
    user_type = fields.Selection(selection=[
        ('vip', 'VIP'),
        ('standard', 'Standard'),
        ('low_cost', 'Low Cost')],
        string="Client Category")
