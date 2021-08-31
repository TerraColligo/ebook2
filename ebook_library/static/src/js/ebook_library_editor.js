odoo.define('ebook_library.form', function (require) {
  var FormEditorRegistry = require('website_form.form_editor_registry');

  FormEditorRegistry.add('download_ebook', {
      defaultTemplateName: 'ebook_library.lead_form',
      defaultTemplatePath: '/ebook_library/static/src/xml/lead_form.xml',
      fields: [{
          name: 'ebook_code',
          type: 'char',
          required: true,
          string: 'eBook Code',
      }],
      successPage: '/ebook-thank-you',
  });

});
