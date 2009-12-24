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
from zope import schema, interface
from zojax.filefield.field import ImageField
from zojax.contenttypes.interfaces import _


class IImage(interface.Interface):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Image title.'),
        required = False)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'A short summary of the image.'),
        required = False)

    data = ImageField(
        title=_(u'Data'),
        description=_(u'The actual content of the image.'),
        required = False)

    size = interface.Attribute('Size')

    width = interface.Attribute('Width')

    height = interface.Attribute('Height')


class IImageType(interface.Interface):
    """ image content type """
