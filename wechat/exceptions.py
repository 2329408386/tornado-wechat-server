#!/usr/bin/env python
# coding=utf-8

__author__ = 'qingfeng'


class WeChatServerException(Exception):
    """异常基类"""
    pass


class ParseError(WeChatServerException):
    """解析微信服务器数据异常"""
    pass
