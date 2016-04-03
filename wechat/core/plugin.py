#!/usr/bin/env python
# coding=utf-8

__author__ = 'qingfeng'


class BasePlugin(object):
    """
    "插件需要有name，description，version，author属性，默认为空。__type__。
    """
    name = ""
    description = ""
    version = ""
    author = ""

    def run(self):
        """
        :return:
        """
        pass
