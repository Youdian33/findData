# coding: UTF-8

import sae
import web
import os


sae.add_vendor_dir('vendor')
from weixinInterface import WeixinInterface

urls = ('/weixin','WeixinInterface')

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates/')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)