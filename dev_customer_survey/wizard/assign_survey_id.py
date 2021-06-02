# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Devintelle Solutions (<http://devintellecs.com/>).
#
##############################################################################

from odoo import api, fields, models, _

class assign_survey(models.TransientModel):
    _name = "assign.survey"
    
    survey_id = fields.Many2one('survey.survey',string="Survey" , required=True)

    def update_survey_id(self):
        res_partner_data = self.env['res.partner'].browse(self._context.get('active_ids'))
        for record in res_partner_data:
            record.survey_id = self.survey_id.id
    def set_send_survey(self):
        res_partner_data = self.env['res.partner'].browse(self._context.get('active_ids'))
        for record in res_partner_data:
            record.survey_id = self.survey_id.id        
            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
