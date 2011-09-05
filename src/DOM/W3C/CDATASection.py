from __future__ import with_statement

import sys, re, string

from DOMException import DOMException
from Text import Text


class CDATASection(Text):
    def __repr__(self):
        return "<CDATA '%s' at 0x%08X>" % (self.tag, id(self))

    @property
    def nodeName(self):
        return "#cdata-section"

    @property
    def nodeType(self):
        return Node.CDATA_SECTION_NODE
