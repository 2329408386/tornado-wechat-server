#!/usr/bin/env python
# coding=utf-8
from wechat.core.plugin import BasePlugin
from wechat.messages import MESSAGE_TYPES, TextMessage
from wechat.reply import TextReply

__author__ = 'qingfeng'
__type__ = "receive_message"
__className__ = "WeatherPlugin"


class WeatherPlugin(BasePlugin):
    name = "天气示例插件"
    description = "天气示例插件"
    version = "1.0"
    author = "dubuqingfeng"

    def run(self, message=None):
        print(message)
        message_type = MESSAGE_TYPES.get(message['type'], TextMessage)
        result = message_type(message)
        return TextReply(result, 'Hello,你是逗比,你刚才说 %s' % result.text).render()
        # return message
