#!/usr/bin/env python
# coding=utf-8
from xml.dom import minidom, Node

__author__ = 'doraemonext'


class XMLStore(object):
    def __init__(self, xmlstring):
        self._raw = xmlstring
        self._doc = minidom.parseString(xmlstring)

    @property
    def xml2dict(self):
        self._remove_whitespace_nodes(self._doc.childNodes[0])
        return self._element2dict(self._doc.childNodes[0])

    def _element2dict(self, parent):
        d = {}
        for node in parent.childNodes:
            if not isinstance(node, minidom.Element):
                continue
            if not node.hasChildNodes():
                continue

            if node.childNodes[0].nodeType == minidom.Node.ELEMENT_NODE:
                try:
                    d[node.tagName]
                except KeyError:
                    d[node.tagName] = []
                d[node.tagName].append(self._element2dict(node))
            elif len(node.childNodes) == 1 and node.childNodes[0].nodeType in [minidom.Node.CDATA_SECTION_NODE, minidom.Node.TEXT_NODE]:
                d[node.tagName] = node.childNodes[0].data
        return d

    def _remove_whitespace_nodes(self, node, unlink=True):
        remove_list = []
        for child in node.childNodes:
            if child.nodeType == Node.TEXT_NODE and not child.data.strip():
                remove_list.append(child)
            elif child.hasChildNodes():
                self._remove_whitespace_nodes(child, unlink)
        for node in remove_list:
            node.parentNode.removeChild(node)
            if unlink:
                node.unlink()
