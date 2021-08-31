# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ # type: ignore
import logging
from odoo.addons.website.models.website import slugify

logger = logging.getLogger(__name__)

# An eBook that has files and images
class EBook(models.Model):
    _name = 'ebook_library.ebook'
    _inherit = ['mail.thread']
    _description = 'eBook'

    name = fields.Char('eBook Name', translate=True, track_visibility='onchange', required=True)
    code = fields.Char('eBook Code', compute='_compute_code', store=True, track_visibility='onchange')
    downloadable_files = fields.One2many('ebook_library.downloadable_file', 'ebook', 'Downloadable Files', track_visibility='onchange')
    ebook_leads = fields.One2many('ebook_library.lead', 'ebook', 'eBook Leads', track_visibility='onchange')

    @api.depends('name')
    def _compute_code(self):
        for item in self:
            item.code = slugify(item.name)
