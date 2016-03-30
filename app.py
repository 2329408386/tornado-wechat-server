#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
from setting import settings

__author__ = 'qingfeng'

if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=urls,
        **settings
    )
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()
