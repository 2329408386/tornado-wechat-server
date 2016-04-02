#!/usr/bin/env python
# coding=utf-8
from .handlers.wechat import WechatHandler

__author__ = 'qingfeng'

urls = [
    [r"/", WechatHandler],
]
