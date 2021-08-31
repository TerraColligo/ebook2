# -*- coding: utf-8 -*-
from odoo import http # type: ignore
from odoo.http import request, Response # type: ignore
import logging
import sys
import traceback
import base64

logger = logging.getLogger(__name__)

class EbookLibrary(http.Controller):
    @http.route('/ebook_library/download', auth='public')
    def download(self, **kwargs):
        ebook_code = kwargs.get('ebook_code', '')
        file_id = kwargs.get('file_id', '')
        uuid = kwargs.get('contact', '')
        if not ebook_code or not file_id or not uuid:
            return Response('Invalid download link', status=403)
        EBook = request.env['ebook_library.ebook']
        ebooks = EBook.sudo().search([('code', '=', ebook_code)])
        if len(ebooks) <= 0:
            return Response('Invalid download link', status=403)
        ebook = ebooks[0]
        leads = ebook.ebook_leads.search([('uuid', '=', uuid)])
        if len(leads) <= 0:
            return Response('Invalid download link', status=403)
        lead = leads[0]
        downloadable_files = ebook.downloadable_files.search([('id', '=', file_id)])
        if len(downloadable_files) <= 0:
            return Response('Invalid download link', status=403)
        downloadable_file = downloadable_files[0]
        data = base64.b64decode(downloadable_file.file)
        response = request.make_response(data, [
            ('Content-Type', downloadable_file.content_type or 'application/octet-stream'),
            ('Content-Disposition', 'attachment; filename="%s"' %(downloadable_file.filename)),
        ])
        logger.info('ACCESS DOWNLOAD LINK FOR %s file %s contact %s' % (ebook.code, downloadable_file.filename, uuid))
        return response
