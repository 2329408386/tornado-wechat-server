#!/usr/bin/env python
# coding=utf-8
import hashlib
from configs import TOKEN
from ..core.handler import BaseHandler
from ..lib.parser import XMLStore
from ..hook import Hook

__author__ = 'qingfeng'


class WeChatHandler(BaseHandler):
    responseStr = ""

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        echo_str = self.get_argument('echostr', '')
        if self.check_signature():
            self.write(echo_str)
        else:
            self.write(self.responseStr)

    def check_signature(self):
        signature = self.get_argument('signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        tmp_array = [TOKEN, timestamp, nonce]
        tmp_array.sort()
        m = hashlib.sha1()
        map(m.update, tmp_array)
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

        result['type'] = result.pop('MsgType').lower()

        self.responseStr = Hook().listen("receive_message", result)

        # message_type = MESSAGE_TYPES.get(result['type'], UnknownMessage)
        # message = message_type(result)
        # self.responseStr = TextReply(message, message.source).render()

        self.write(self.responseStr)
