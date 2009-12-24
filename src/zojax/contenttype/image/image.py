##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" page interfaces

$Id$
"""
from zope import interface, component
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.lifecycleevent.interfaces import IObjectCopiedEvent
from zojax.content.type.item import PersistentItem
from zojax.content.type.contenttype import ContentType
from zojax.filefield.field import FileFieldProperty
from zojax.filefield.interfaces import IFile as IFileData


from interfaces import IImage


class Image(PersistentItem):
    interface.implements(IImage)

    data = FileFieldProperty(IImage['data'])

    @property
    def size(self):
        if self.data is not None:
            return self.data.size
        else:
            return 0

    @property
    def width(self):
        if self.data is not None:
            return self.data.width
        else:
            return -1

    @property
    def height(self):
        if self.data is not None:
            return self.data.height
        else:
            return -1


class Sized(object):
    component.adapts(IImage)
    interface.implements(ISized)

    def __init__(self, context):
        self.context = context

    def sizeForSorting(self):
        return "byte", self.context.size

    def sizeForDisplay(self):
        return byteDisplay(self.context.size)


class ImageType(ContentType):

    def add(self, content, name=''):
        if not name and content is not None:
            try:
                name = content.data.filename.split('\\')[-1].split('/')[-1]
            except AttributeError:
                pass
        return super(ImageType, self).add(content, name)
