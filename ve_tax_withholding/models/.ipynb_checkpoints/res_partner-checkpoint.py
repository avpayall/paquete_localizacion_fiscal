# -*- coding: utf-8 -*- 

from odoo import models, fields, api 

class ResPartner(models.Model):
    
    _inherit = 'res.partner' 
    
    partner_type_custom = fields.Selection([('PNR','Persona Natural Residente'),
                                            ('PNNR','Persona Natural No Residente'), 
                                            ('PJD','Persona Juridica Dominciliada'), 
                                            ('PJDN','Persona Juridica No Domicialda'), 
                                            ('PJNCD','Persona Juridica No Costituida Domicilada')],
                                           string='partner custom', store=True, )
    
    
            
    

            
    