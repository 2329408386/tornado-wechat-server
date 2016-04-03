#!/usr/bin/env python
# coding=utf-8
from importlib import import_module

__author__ = 'qingfeng'

plugins = {}


class Hook(object):
    @staticmethod
    def listen(hook_str=None, message=None):
        if hook_str in plugins.keys():
            hook_list = plugins[hook_str]
            if isinstance(hook_list, list):
                for index in range(len(hook_list)):
                    module = import_module('.%s' % hook_list[index], "plugins")
                    print(dir(module))
                    a_class = getattr(module, getattr(module, "__className__"))
                    result = a_class().run(message)
                    if result:
                        return result
        else:
            return False
