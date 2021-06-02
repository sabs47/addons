# © 2019 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.http import Controller, route, request
from odoo.addons.web.controllers.main import Binary


class WebsiteSnippet(Controller):

    @route(
        '/website_snippet/thumbnail/<int:sid>',
        type='http',
        auth='user',
        website=True,
    )
    def website_snippet_thumbnail(self, sid, **kw):
        kw['model'] = 'website_snippet.snippet'
        kw['field'] = 'thumbnail_small'
        kw['id'] = sid

        return Binary().content_image(**kw)

    @route(
        '/website_snippet/website_snippet.css',
        type='http',
        auth='public',
    )
    def website_snippet_css(self, **kw):
        content = request.env['website_snippet.snippet'].get_css()

        headers = [
            ('Cache-Control', 'no-cache'),
            ('Content-Type', 'text/css; charset=utf-8'),
        ]
        headers.append(('Content-Length', len(content)))

        response = request.make_response(content, headers)
        return response

    @route(
        '/website_snippet/website_snippet.js',
        type='http',
        auth='public',
    )
    def website_snippet_js(self, **kw):
        content = request.env['website_snippet.snippet'].get_js()

        headers = [
            ('Cache-Control', 'no-cache'),
            ('Content-Type', 'application/javascript'),
        ]
        headers.append(('Content-Length', len(content)))

        response = request.make_response(content, headers)
        return response
