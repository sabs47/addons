from odoo import http

class Academy(http.Controller):
    @http.route('/offres/offres/', auth='public')
    def index(self, **kw):
        return "Recrutement offres"