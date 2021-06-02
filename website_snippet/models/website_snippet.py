# © 2018 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, tools
from odoo.tools.image import image_process

PLACEHOLDER = '''
iVBORw0KGgoAAAANSUhEUgAAAGQAAABPCAIAAACS6/f2AAAAGXRFWH
RTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAA
AAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+ID
x4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3
JlIDUuMC1jMDYxIDY0LjE0MDk0OSwgMjAxMC8xMi8wNy0xMDo1NzowMSAgICAgICAgIj4gPHJkZj
pSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbn
MjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYW
RvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS
4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZX
NvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNS4xIE1hY2ludG
9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoyNEM1RERCRDE1N0QxMUU0OTRGOERBMjU0QT
Q5NTg1NSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDoyNEM1RERCRTE1N0QxMUU0OTRGOERBMj
U0QTQ5NTg1NSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOj
I0QzVEREJCMTU3RDExRTQ5NEY4REEyNTRBNDk1ODU1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZG
lkOjI0QzVEREJDMTU3RDExRTQ5NEY4REEyNTRBNDk1ODU1Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPi
A8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+leM1cAAAAo1JREFUeN
rs2lFL40AUhmG7DfSi0KWFihGFgkJFQXHB/f9/wcrKerWBFVMsVAy0GKh0XzMSgpo0je0kXb9zEd
LSaZyHc2ZOUmvz+XxLkS++iUBYwhKWsIQlLBEIS1jCEpawhCUCYQlLWMISlrBEICxhCUtYwhKWCI
S1lnCq/Mf9ur6eTCau6+7v7SmzsiIMQ6Q42e52VYYL4n404thsNhuNhrAWxHg85titTFpVFwspyt
BxnE67/dWxKDHP87KwHh44IoVX/CZDTG1+ld2Q2fq+T9a0Wq20z8xmM1ODnU4n+f5TGJrh7I+lrP
r2sIIg+ON5ML1c1XG+p2ONovRhXX8DypDpdMo3kGJo7rpuhvimYsF05/scDZO7s8OynayvD2vwfe
6QUAyE0h8OgyjAsklWW+v/lC7LRNBb0YtycnZ6mtY0UKeGjBNeWiNbF1YBpuQqzmp1eHCQ/Un7ZK
svQ9YU1qYCTMkazDPnly+3W5irzCyY2KrM7l6AKW4pGPLj/HypS9vJslVm1uVgUJgpLt5iXfuHWf
bz4uK/7eBJzNf26hNde91x6vX6BizwzPbv7a2ZcIH8ooQZzp3zyfHxspe2U4ar3w0L74NUMdy9Xm
+p7tzmnliV1oFP/r654YSlPWcy2m8dqtKUmvaKnCKzKshkAysnGXMeXF1xPOr3s+dcFpM9rDQyNv
tke8XNDbc42TtAWUy2nzq0ooifPTwGQYxlHjMsXNcZglQpTOU8z2KSpA+pNI1+jNhK/DDx5unV+6
CrKIvJdhmmBb0V5ZXnzrn0KL+Df44qq1LP2qubWRsU+vleWMISlrCEpRCWsIQlLGEJSyEsYQlLWM
ISlkJYwhKWsIQlLIWwhLWe+CfAAMPU4Nfn8LNdAAAAAElFTkSuQmCC
'''


class WebsiteSnippet(models.Model):

    _name = 'website_snippet.snippet'

    name = fields.Char(
        required=True,
    )

    html_text = fields.Text(
        string="HTML",
        required=True,
        compute='_compute_html_text',
        inverse='_inverse_html_text',
    )

    html = fields.Html(
        string="HTML",
        sanitize=False,
    )

    css = fields.Text(
        string="CSS",
    )

    js = fields.Text(
        string="JavaScript",
    )

    thumbnail = fields.Binary()
    thumbnail_small = fields.Binary(
        compute='_compute_thumbnail_small',
    )

    @api.depends('thumbnail')
    def _compute_thumbnail_small(self):
        for rec in self:
            rec.thumbnail_small = image_process(
                rec.thumbnail or PLACEHOLDER,
                (100, None),
            )

    @api.model
    def get_css(self):
        snippets = self.search([])
        css = ''
        for snippet in snippets:
            css += snippet.css and str(snippet.css) or ''

        return "#website_snippet { }\n%s" % css

    @api.model
    def get_js(self):
        snippets = self.search([])

        # build base
        base_js = """
%s
odoo.define('website_snippet.snippets', function(require) {
    "use strict";
    var snippets = []
    %s
    return snippets;
});
        """

        # build defines
        defines = ""
        for snippet in snippets:
            snippet_id = snippet.id
            name = snippet.name or 'Undefined'
            html = snippet.html or ''
            html = html.replace("\n", '')
            html = '<div class="container website_snippet_%s">%s</div>' % (
                snippet_id,
                html,
            )
            js = snippet.js or ''

            defines += """
odoo.define('website_snippet.snippet_{snippet_id}', function(require) {{
    "use strict";
    {js}

    return {{
        'id': {snippet_id},
        'name': "{name}",
        'html': "{html}",
    }}
}});
        """.format(**{
                'snippet_id': snippet_id,
                'name': name.replace('"', '\\"'),
                'html': html.replace('"', '\\"'),
                'js': js,
            })

        # build requires
        requires = ""
        for snippet in snippets:
            requires += """
    snippets['snippet_%s'] = require('website_snippet.snippet_%s');
        """ % (snippet.id, snippet.id)

        return base_js % (defines, requires)

    def _compute_html_text(self):
        for rec in self:
            rec.html_text = rec.html

    def _inverse_html_text(self):
        for rec in self:
            rec.html = tools.html_sanitize(
                rec.html_text,
                sanitize_tags=False,
                sanitize_attributes=False,
                sanitize_style=False,
                strip_style=False,
                strip_classes=False,
            )
