# -*- coding: utf-8 -*-
from odoo import http

# class SaleTierValidation(http.Controller):
#     @http.route('/sale_tier_validation/sale_tier_validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_tier_validation/sale_tier_validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_tier_validation.listing', {
#             'root': '/sale_tier_validation/sale_tier_validation',
#             'objects': http.request.env['sale_tier_validation.sale_tier_validation'].search([]),
#         })

#     @http.route('/sale_tier_validation/sale_tier_validation/objects/<model("sale_tier_validation.sale_tier_validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_tier_validation.object', {
#             'object': obj
#         })