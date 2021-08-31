# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ # type: ignore
import logging

logger = logging.getLogger(__name__)

# Extend CRM Lead object to add eBook Library support
class Lead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'mail.thread']

    is_ebook_lead = fields.Boolean('Is eBook Lead', track_visibility='onchange')
    ebook_leads = fields.One2many('ebook_library.lead', 'crm_lead', 'eBook Leads', track_visibility='onchange')
