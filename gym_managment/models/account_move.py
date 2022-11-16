from odoo import fields, models, api


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super(AccountMoveInherit, self).action_post()

        if not self.partner_id.is_coach:

            if self.amount_total >= 100:
                self.partner_id.user_type = 'vip'
                return res
            if self.amount_total >= 50:
                self.partner_id.user_type = 'standard'
                return res
            else:
                self.partner_id.user_type = 'low_cost'
                return res
