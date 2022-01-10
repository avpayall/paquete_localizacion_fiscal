# -*- coding: utf-8 -*-
from odoo import models, fields, api
class AccountMove( models.Model):
    _inherit = 'account.move'
    control_number = fields.Char(string='Numero de control', required=True, default='00')
    
    @api.model
    def _withholdings(self):
    	view_id = self.env.ref('tax.withholding_voucher_vendor.tax_withholding_form').id
    	context = self._context.copy()
    	return {
            'name':'form_name',
            'view_type':'form',
            'view_mode':'tree',
            'views' : [(view_id,'form')],
            'res_model':'model_name',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'res_id':self.id,
            'target':'new',
            'context':context,
        }
