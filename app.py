#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
from setting import settings
from wechat.plugin_manager import PluginManager
from wechat.route import urls

__author__ = 'qingfeng'

if __name__ == "__main__":
    plugin_manager = PluginManager()
    plugin_manager.load_plugins()
    application = tornado.web.Application(
        handlers=urls,
        **settings
    )
    application.listen(9999)
    tornado.ioloop.IOLoop.current().start()
