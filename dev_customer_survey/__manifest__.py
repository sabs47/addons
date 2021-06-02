# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Devintelle Solutions (<http://devintellecs.com/>).
#
##############################################################################

{
    'name': 'client',
    'version': '13.0.1.0',
    'sequence': 1,
    'category': 'Marketing',
    'description':
        """
This module is integrated with the survey module
        to allow you to define Survey for Customer
        
        Customer survey, User Customer survey, Survey, Customer, user, Customer multiple suervey, survey customer, 
Customer Survey
Odoo Customer Survey
Customers survey 
Odoo customers survey
Manage customer survey 
Odoo manage customer survey 
Define a survey on customer Screen
Odoo Define a survey on customer Screen
Multiple Survey for one customer
Odoo Multiple Survey for one customer
Send survey Invitation mail to customer mailbox 
Odoo Send survey Invitation mail to customer mailbox 
Print Survey Feedback on customer screen 
Odoo Print Survey Feedback on customer screen 
Multiple survey history on customer screen 
Odoo Multiple survey history on customer screen 
Print customer survey 
Odoo print customer survey 
Customer form 
Odoo customer form 
Manage customer form 
Odoo manage customer form 
Print customer form 
Odoo print customer form
Customer survey history 
Odoo customer survey history 
Print customer survey history 
Odoo print customer survey history 
Manage customer survey history 
Odoo manage customer survey history 
        

    """,
    'summary': 'Odoo App will help to make multiple survey for customer',
    'depends': ['survey'],
    'data': [
         'views/res_partner_views.xml',
         'data/survey_mail_template.xml',
         'wizard/assign_survey_id_wizard.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    #'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    #author and support Details
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':29.0,
    'currency':'EUR',
  #  'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
