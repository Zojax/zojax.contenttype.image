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
"""

$Id$
"""
from zope import interface, component
from zope.size.interfaces import ISized
from zojax.content.forms.form import AddForm
from zojax.content.type.interfaces import IContentViewView

from zojax.contenttype.image.interfaces import IImage


class AddImageForm(AddForm):

    def getName(self, object=None):
        name = super(AddImageForm, self).getName()
        if not name and object is not None:
            try:
                name = object.data.filename
            except:
                pass

        return name


class ImageView(object):

    def size(self):
        return ISized(self.context).sizeForDisplay()


class ImageDownload(object):

    def show(self):
        try:
            return self.context.data.show(
                self.request,
                filename=self.context.__name__,
                contentDisposition='inline')
        except:
            return u''


class ImageViewView(object):
    interface.implements(IContentViewView)
    component.adapts(IImage, interface.Interface)

    name = u'index.html'

    def __init__(self, image, request):
        pass
