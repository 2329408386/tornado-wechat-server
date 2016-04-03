#!/usr/bin/env python
# coding=utf-8
from wechat.core.plugin import BasePlugin
from wechat.messages import MESSAGE_TYPES, UnknownMessage
from wechat.reply import TextReply

__author__ = 'qingfeng'
__type__ = "receive_message"
__className__ = "SamplePlugin"


class SamplePlugin(BasePlugin):
    name = "示例插件"
    description = "示例插件"
    version = "1.0"
    author = "dubuqingfeng"

    def run(self, message=None):
        print(message)
        message_type = MESSAGE_TYPES.get(message['type'], UnknownMessage)
        result = message_type(message)
        return TextReply(result, result.source).render()
        # return message
