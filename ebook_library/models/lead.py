# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ # type: ignore
import logging
import uuid

logger = logging.getLogger(__name__)

# Our own lead object that the website form creates
class Lead(models.Model):
    _name = 'ebook_library.lead'
    _inherit = ['mail.thread']
    _description = 'eBook Lead'

    name = fields.Char(track_visibility='onchange')
    email = fields.Char(track_visibility='onchange')
    ebook_code = fields.Char(track_visibility='onchange')
    uuid = fields.Char(track_visibility='onchange')
    ebook = fields.Many2one('ebook_library.ebook', 'eBook', track_visibility='onchange')
    crm_lead = fields.Many2one('crm.lead', 'CRM Lead', track_visibility='onchange')

    @api.model
    def create(self, values):
        # Assign random uuid value for verification
        values['uuid'] = uuid.uuid4().hex
        # Search the chosen eBook by code
        EBook = self.env['ebook_library.ebook']
        ebooks = EBook.search([('code', '=', values['ebook_code'])])
        ebook = ebooks[0]
        values['ebook'] = ebook.id
        # Create the Odoo CRM Lead
        CRMLead = self.env['crm.lead']
        crm_lead = CRMLead.create({
            'name': values['name'],
            'email_from': values['email'],
            'is_ebook_lead': True,
        })
        values['crm_lead'] = crm_lead.id
        # Create the eBook lead
        ebook_lead = super(Lead, self).create(values)
        # Send download email
        template_id = self.env.ref('ebook_library.ebook_download_email')
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        download_url = '%s/ebook_library/download?ebook_code=%s&contact=% s' % (base_url, ebook.code, values['uuid']) # will be appended with &file_id=x when looping files
        email_from = self.env.company.email
        msg = ebook_lead.with_context(email_from=email_from, download_url=download_url).message_post_with_template(template_id.id)
        return ebook_lead
