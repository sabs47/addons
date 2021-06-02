from odoo import http

class Academy(http.Controller):
    @http.route('/offres/equipement_pedagogique/', auth='public')
    def index(self, **kw):
        return "équipement pédagogique"
