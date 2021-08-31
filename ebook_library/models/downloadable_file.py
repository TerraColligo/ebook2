# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ # type: ignore
import logging

logger = logging.getLogger(__name__)

# Downloadable eBook file (usually PDF)
class DownloadableFile(models.Model):
    _name = 'ebook_library.downloadable_file'
    _inherit = ['mail.thread']
    _description = 'Downloadable eBook File'

    file = fields.Binary(track_visibility='onchange', required=True)
    filename = fields.Char(track_visibility='onchange', required=True)
    content_type = fields.Char(track_visibility='onchange', default='application/pdf', required=True)
    ebook = fields.Many2one('ebook_library.ebook', 'eBook', track_visibility='onchange')
