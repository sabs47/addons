/* © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */
odoo.define('website_snippet.editor', function(require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var options = require('web_editor.snippets.options');
    var editor = require('web_editor.snippet.editor');
    var snippets = require('website_snippet.snippets');
    var widget = require('web_editor.widget');
    var Ace = require('web_editor.ace');
    var WebsiteNewMenu = require('website.newMenu');
    var DebugManager = require('web.DebugManager');

    var _t = core._t;
    var QWeb = core.qweb;

    ajax.loadXML('/website_snippet/static/src/xml/templates.xml', QWeb);

    editor.Class.include({
        _computeSnippetTemplates: function(html) {
            var $html = $('<div/>').append(html);

            for (var i in snippets) {
                var snippet = '<div name="' + snippets[i].name + '" data-oe-type="snippet" data-oe-thumbnail="/website_snippet/thumbnail/' + snippets[i].id + '">' +
                    '<section class="snippet-snippet website_snippet_' + snippets[i].id + '">' + snippets[i].html + '</section>' +
                    '</div>';
                $html.find('#snippet_snippets .o_panel_body').append(snippet);
            }
            return this._super($html.html());
        },
    });

    function raise_validation(message) {
        var err_dialog = new widget.Dialog(self, {
            title: _t('Validation Error'),
            $content: '<p>' + message + '</p>',
            buttons: [{
                text: _t("OK"),
                close: true
            }]
        });
        err_dialog.open()
    }

    var NewSnippetDialog = widget.Dialog.extend({
        start: function() {
            var self = this;
            var sup = self._super;
            if (!window.ace && !self.loadJS_def) {
                self.loadJS_def = ajax.loadJS('/web/static/lib/ace/ace.js').then(function() {
                    return $.when(
                        ajax.loadJS('/web/static/lib/ace/mode-xml.js'),
                        ajax.loadJS('/web/static/lib/ace/mode-scss.js'),
                        ajax.loadJS('/web/static/lib/ace/theme-monokai.js'),
                    );
                });
            }
            return $.when(self.loadJS_def).then(function() {
                self.htmlEditor = window.ace.edit(self.$el.find("#ws-html-view-editor")[0]);
                self.htmlEditor.setTheme("ace/theme/monokai");
                self.htmlEditor.getSession().setUseWorker(false);
                self.htmlEditor.getSession().setMode("ace/mode/xml");

                self.cssEditor = window.ace.edit(self.$el.find("#ws-css-view-editor")[0]);
                self.cssEditor.setTheme("ace/theme/monokai");
                self.cssEditor.getSession().setUseWorker(false);
                self.cssEditor.getSession().setMode("ace/mode/scss");

                sup();
            });
        },
        save: function() {
            var self = this;

            var title = this.$el.find("[name='ws_title']").val();
            var html = this.htmlEditor.getValue();
            var css = this.cssEditor.getValue();

            var valid = true;

            if (this.$el.find("[name='ws_title']")[0].checkValidity()) {

                try {
                    var json = JSON.stringify(html);
                    JSON.parse(json);
                    var valid = true;
                } catch (e) {
                    var valid = false;
                }

                if (valid) {
                    ajax.jsonRpc('/web/dataset/call_kw', 'call', {
                        model: 'website_snippet.snippet',
                        method: 'create',
                        args: [{
                            'name': title,
                            'html_text': html,
                            'css': css,
                        }],
                        kwargs: {}
                    }).then(function() {
                        var debugManager = new DebugManager(self);
                        debugManager.regenerateAssets();
                    });
                } else {
                    raise_validation(_t('There is an error in your HTML code.'));
                }
            } else {
                raise_validation(_t('Please enter valid title for the building block.'));
            }
        }
    });

    WebsiteNewMenu.include({
        actions: _.extend({}, WebsiteNewMenu.prototype.actions || {}, {
            new_snippet: '_createNewSnippet',
        }),
        _createNewSnippet: function() {
            var self = this;
            var dialog = new NewSnippetDialog(self, {
                title: _t('New Building Block'),
                $content: QWeb.render('website_snippet.new')
            });
            dialog.open()
        },
    });

    options.registry.custom_snippet = options.Class.extend({
        on_prompt: function() {
            var self = this;
            var dialog = new NewSnippetDialog(self, {
                title: _t('New Building Block'),
                $content: QWeb.render('website_snippet.new')
            });
            dialog.open()
        },

        onBuilt: function() {
            this.on_prompt();
            this.onRemove();
            this._super();
        },

        editHtml: function(previewMode) {
            this.on_prompt();
        },

        createSnippet: function(previewMode) {
            this.on_prompt_save();
        }

    });

    editor.Class.include({
        _registerDefaultTexts: function($in) {
            if ($in === undefined) {
                $in = this.$snippets.find('.oe_snippet_body');
            }

            if ($in.hasClass('snippet-snippet')){
                var elements = $in.find('*:not(iframe)');
            } else {
                var elements = $in.find('*');
            }

            elements.addBack()
                .contents()
                .filter(function() {
                    return this.nodeType === 3 && this.textContent.match(/\S/);
                }).parent().addClass('o_default_snippet_text');
        },
    });
});
