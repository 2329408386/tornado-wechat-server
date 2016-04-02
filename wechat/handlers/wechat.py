#!/usr/bin/env python
# coding=utf-8
import hashlib
from configs import TOKEN
from ..core.handler import BaseHandler
from ..messages import MESSAGE_TYPES, UnknownMessage
from ..reply import TextReply
from ..lib.parser import XMLStore

__author__ = 'qingfeng'


class WechatHandler(BaseHandler):
    responseStr = ""

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        echostr = self.get_argument('echostr', '')
        if self.check_signature():
            self.write(echostr)
        else:
            self.write(self.responseStr)

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

    def post(self, *args, **kwargs):
        if self.check_signature() is False:
            self.write(self.responseStr)
        xml_data = self.request.body

        xml_str = XMLStore(xmlstring=xml_data)
        result = xml_str.xml2dict
        print(result)
        result['type'] = result.pop('MsgType').lower()

        message_type = MESSAGE_TYPES.get(result['type'], UnknownMessage)
        message = message_type(result)
        self.responseStr = TextReply(message, message.source)
        self.write(self.responseStr)
        pass
