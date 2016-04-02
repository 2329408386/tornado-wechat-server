#!/usr/bin/env python
# coding=utf-8
import hashlib
from configs import TOKEN
from ..core.handler import BaseHandler

__author__ = 'qingfeng'


class WechatHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        echostr = self.get_argument('echostr', '')
        if self.check_signature():
            self.write(echostr)
        pass

    def check_signature(self):
        signature = self.get_argument('signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        tmpArray = [TOKEN, timestamp, nonce]
        tmpArray.sort()
        m = hashlib.sha1()
        map(m.update, tmpArray)
        hashcode = m.hexdigest()
        if hashcode == signature:
            return True
        return False
