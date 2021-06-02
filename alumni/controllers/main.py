from odoo import http

class Academy(http.Controller):
    @http.route('/offres/alumni/', auth='public')
    def index(self, **kw):
        return "offres alumni"
