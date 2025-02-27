# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: ADVAITH BG (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class Product(models.Model):
    """Class to add fields like quantity,views,top-selling and
    most-viewed to product.template model"""
    _inherit = 'product.template'

    qty_sold = fields.Integer(string='Quantity sold',
                              help="Quantity Sold")
    views = fields.Integer(string='Views', help="Total Views")
    top_selling = fields.Boolean(string='TopSelling',
                                 help="If top selling product")
    most_viewed = fields.Boolean(string='Most Viewed',
                                 help="If most viewed product")
