# -*- coding: utf-8 -*-
from odoo import http

# class TestLibrary(http.Controller):
#     @http.route('/test_library/test_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_library/test_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_library.listing', {
#             'root': '/test_library/test_library',
#             'objects': http.request.env['test_library.test_library'].search([]),
#         })

#     @http.route('/test_library/test_library/objects/<model("test_library.test_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_library.object', {
#             'object': obj
#         })