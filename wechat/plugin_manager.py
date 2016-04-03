#!/usr/bin/env python
# coding=utf-8
from importlib import import_module
import os
from . import hook

__author__ = 'qingfeng'


class PluginManager(object):

    def __init__(self, plugins=(), config=None):
        if not config:
            config = {}
        default_directory = os.path.join(os.path.dirname(__file__), "../plugins")
        self.directories = config.get("directories", (default_directory,))

    def load_plugins(self):
        """Load plugins by iterating files in plugin directories.
        """
        plugins = []
        for dir in self.directories:
            try:
                for f in os.listdir(dir):
                    if f.endswith(".py") and f != "__init__.py":
                        plugins.append((f[:-3], dir))
            except OSError:
                print("Failed to access: %s" % dir)
                continue

        fh = None
        mod = None
        for (name, dir) in plugins:
            mod = import_module('.%s' % name, "plugins")
            if hasattr(mod, "__type__"):
                print('__type__', mod.__type__)
                if mod.__type__ in hook.plugins.keys():
                    hook.plugins.setdefault(mod.__type__, []).append(name)
                else:
                    hook.plugins[str(mod.__type__)] = [name]
        print(hook.plugins)
