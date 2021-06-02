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

    def send_survey_mail(self,partner_id):
        template_pool = self.env['mail.template']
        mail_template_id = self.env['ir.model.data'].get_object_reference('dev_customer_survey', 'res_partner_survey_template')[1]
        print ("mail_template_id===",mail_template_id)
        print ("partner_id===",partner_id)
        if mail_template_id:
            mtp = template_pool.browse(mail_template_id)
            mtp.send_mail(partner_id,force_send=True)
            print ("mtp===",mail_template_id)
        return True
        
        
    def asign_survey_template(self):
        active_id = self._context.get('active_ids')
        res_partner_data = self.env['res.partner'].browse(active_id)
        res_partner_data.survey_id = self.survey_id.id
        print ("res_partner_data.survey_id=======",res_partner_data.survey_id)
        for record in res_partner_data:
            print ("record=======",record)
            self.send_survey_mail(record.id)
            record.survey_id = self.survey_id.id
        return True
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
