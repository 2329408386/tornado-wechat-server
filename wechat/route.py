#!/usr/bin/env python
# coding=utf-8
from .handlers.wechat import WeChatHandler

__author__ = 'qingfeng'

urls = [
    [r"/", WeChatHandler],
]
