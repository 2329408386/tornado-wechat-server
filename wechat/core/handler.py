#!/usr/bin/env python
# coding=utf-8
import tornado.web

__author__ = 'qingfeng'


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write("test")
