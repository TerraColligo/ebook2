# -*- coding: utf-8 -*-
# Developed By Haresh Chavda <chavdaharesh69@gmail.com>


from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sort_product_type = fields.Selection([
        ('default', 'No Sorting (Odoo Default)'), 
        ('alphabet', 'Sort Alphabetically')], 
        default='default')
    sort_by = fields.Selection([
        ('product_ref', 'Product Reference'),
        ('product_name', 'Product Name'),
        ], default='product_ref')
    group_by = fields.Selection([
        ('no_group_by', 'No Grouping'),
        ('categ', 'Group by 1st level category'),
        ], default='no_group_by')

    def get_category_group_data(self):
        category_data_dict = {}
        for line in self.move_ids_without_package:
            if line.product_id.categ_id.id not in category_data_dict:
                category_data_dict[line.product_id.categ_id.id] = {
                    'lines': [line],
                    'category_name': line.product_id.categ_id.name,
                    'product_uom_qty': line.product_uom_qty,
                }
            else:
                category_data_dict[line.product_id.categ_id.id]['lines'].append(line)
                category_data_dict[line.product_id.categ_id.id]['product_uom_qty'] += line.product_uom_qty
        final_list = []
        for i in category_data_dict:
            final_list.append(category_data_dict.get(i))
        
        final_list = sorted(final_list, key = lambda i: i.get('category_name'))
        for i in final_list:
            sort_lines = i.get('lines')
            if self.sort_by == 'product_ref':
                sort_lines = sorted(i.get('lines'), key = lambda i: i.product_id.default_code)
            elif self.sort_by == 'product_name':
                sort_lines = sorted(i.get('lines'), key = lambda i: i.product_id.name)
            i['lines'] = sort_lines
        print("===final_list==", final_list)
        return final_list

    def get_category_group_data_move_line_ids(self, move_line_ids):
        category_data_dict = {}
        for line in move_line_ids:
            print("==line==", line.read())
            if line.product_id.categ_id.id not in category_data_dict:
                category_data_dict[line.product_id.categ_id.id] = {
                    'lines': [line],
                    'category_name': line.product_id.categ_id.name,
                    'product_uom_qty': line.qty_done,
                }
            else:
                category_data_dict[line.product_id.categ_id.id]['lines'].append(line)
                category_data_dict[line.product_id.categ_id.id]['product_uom_qty'] += line.qty_done
        final_list = []
        for i in category_data_dict:
            final_list.append(category_data_dict.get(i))
        
        final_list = sorted(final_list, key = lambda i: i.get('category_name'))
        for i in final_list:
            sort_lines = i.get('lines')
            if self.sort_by == 'product_ref':
                sort_lines = sorted(i.get('lines'), key = lambda i: i.product_id.default_code)
            elif self.sort_by == 'product_name':
                sort_lines = sorted(i.get('lines'), key = lambda i: i.product_id.name)
            i['lines'] = sort_lines
        print("===final_list==", final_list)
        return final_list
