import sys
if sys.version_info >= (2, 7):
    import unittest
else:
    import unittest2 as unittest
try:
    from itertools import ifilterfalse as filterfalse
except ImportError:
    from itertools import filterfalse
if sys.version_info >= (3, 0):
    import urllib as urllib2
else:
    import urllib2