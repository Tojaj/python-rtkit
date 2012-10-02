import urllib
from rtkit.utils import cookielib, build_opener, HTTPCookieProcessor, Request
from rtkit.utils import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler


__all__ = [
    'BasicAuthenticator',
    'CookieAuthenticator',
    'KerberosAuthenticator',
]


class AbstractAuthenticator(object):
    def __init__(self, username, password, url, *handlers):
        self.opener = build_opener(*handlers)
        self.username = username
        self.password = password
        self.url = url
        self._logged = True

    def login(self):
        if self._logged:
            return
        self._login()
        self._logged = True

    def _login(self):
        raise NotImplementedError

    def open(self, request):
        self.login()
        return self.opener.open(request)


class BasicAuthenticator(AbstractAuthenticator):
    def __init__(self, username, password, url):
        passman = HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, username, password)
        super(BasicAuthenticator, self).__init__(
            username, password, url,
            HTTPBasicAuthHandler(passman)
        )


class CookieAuthenticator(AbstractAuthenticator):
    def __init__(self, username, password, url):
        super(CookieAuthenticator, self).__init__(
            username, password, url,
            HTTPCookieProcessor(cookielib.LWPCookieJar())
        )
        self._logged = False

    def _login(self):
        data = {'user': self.username, 'pass': self.password}
        self.opener.open(
            Request(self.url, urllib.urlencode(data))
        )


class KerberosAuthenticator(AbstractAuthenticator):
    def __init__(self, username, password, url):
        try:
            from urllib2_kerberos import HTTPKerberosAuthHandler
        except ImportError:
            raise ImportError('You need urllib2_kerberos, try: pip install urllib2_kerberos')

        super(KerberosAuthenticator, self).__init__(
            username, password, url,
            HTTPKerberosAuthHandler()
        )
