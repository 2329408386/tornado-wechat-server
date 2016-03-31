#!/usr/bin/env python
# coding=utf-8
from wechat.core.handler import BaseHandler

__author__ = 'qingfeng'


class WechatHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        hook.add()
        pass
