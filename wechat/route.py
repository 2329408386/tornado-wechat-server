#!/usr/bin/env python
# coding=utf-8
from wechat.handlers import wechat

__author__ = 'qingfeng'

urls = [
    (r"/", wechat.WechatHandler),
]

