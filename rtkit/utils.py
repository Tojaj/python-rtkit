import sys
if sys.version_info >= (2, 7):
    import unittest
else:
    import unittest2 as unittest

try:
    from itertools import ifilterfalse as filterfalse
except ImportError:
    from itertools import filterfalse

if sys.version_info < (3, 0):
    import cookielib
    from urllib2 import build_opener
    from urllib2 import HTTPPasswordMgrWithDefaultRealm
    from urllib2 import HTTPBasicAuthHandler
    from urllib2 import HTTPCookieProcessor
    from urllib2 import Request
    from urllib2 import HTTPError
else:
    import http.cookiejar as cookielib
    from urllib.request import build_opener
    from urllib.request import HTTPPasswordMgrWithDefaultRealm
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPCookieProcessor
    from urllib.request import Request
    from urllib.error import HTTPError
