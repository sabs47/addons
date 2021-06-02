from odoo import http

class Academy(http.Controller):
    @http.route('/offres/equipe_pedagogique/', auth='public')
    def index(self, **kw):
        return "équipe pédagogique"
