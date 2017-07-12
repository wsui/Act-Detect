#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'wen'

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

port = 8000
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_http on port:" + str(httpd.server_port))
httpd.serve_forever()
