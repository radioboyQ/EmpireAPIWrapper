import json
import requests
from .Exceptions import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class utilties(object):
    """Utility HTTP methods"""

    def check_version(self):
        """
        Check the version of Empire
        :param token: Token for authentication
        :return: Version number
        :return type: str
        """
        version_url = '/api/version'
        full_url = self._url_builder(version_url)
        resp = methods.get(full_url, self.sess)
        return resp

class admin(object):
    """Administrative functions"""

    def _login(self):
        """
        Obtain a token from the server for future requests
        :return: Token
        """
        login_url = '/api/admin/login'
        full_url = self._url_builder_no_token(login_url)
        resp = methods.post(full_url, self.sess, data={'username': self.uname, 'password': self.passwd})
        login_token_dict = resp.json()
        return login_token_dict['token']

    def getPermToken(self):
        """
        Get the permanent token for the server
        :return: Permanent token
        """
        perm_token_url = 'api/admin/permanenttoken'
        full_url = self._url_builder(perm_token_url)
        resp = methods.get(full_url, self.sess)
        perm_token_dict = resp.json
        print(perm_token_dict)


class empireAPI(utilties, admin):

    def __init__(self, host, port=1337, verify=False, token=None, uname=None, passwd=None):
        """
        Information for the start of the class. You must include either a tolken or a username and password
        :param host: IP or domain name to connect to
        :param port: Port to connect to
        :param verify: Requests verify the SSL chain
        :param token: Tolken to authenticate with
        :param uname: Username to authenticate with
        :param passwd: Password to authenticate with
        """

        # No parameters provided
        if token is None and uname is None and passwd is None:
            raise NoAuthenticationProvided('No authentication was provided.')
        elif token is None and (uname is None or passwd is None): # Either uname or passwd but not both and no token
            raise NoAuthenticationProvided('Incomplete authentication provided.')

        # Check if host starts with 'https://' or 'http://'
        if not (host.startswith('https://') or host.startswith('http://')):
            # Append 'https:// to the beginning of the host
            host = 'https://{}'.format(host)


        self.host = host
        self.port = port
        self.verify = verify
        self.token = token
        self.uname = uname
        self.passwd = passwd
        # We should have all of the information needed now to open a connection

        # Other variables to use
        self.perm_token = None
        # Create the session for Requests and consistency
        self.sess = requests.Session()
        self.sess.verify = False
        self.sess.headers = {'Content-Type': 'application/json'}

        # If token is provided, check the version
        if token is not None:
            self._checkToken()
        else:
            # If username and password are provided, get a token
            self.token = admin._login(self)

    def _url_builder(self, resource_location):
        """
        Builds the complete URI
        :param resource_location: Leading slash all the way to but not including the ?
        :return: URI in a string.
        """
        return '{base}:{port}{location}?token={token}'.format(base=self.host, port=self.port,
                                                              location=resource_location, token=self.token)

    def _url_builder_no_token(self, resource_location):
        """
        Builds a URL without a token parameter at the end
        :param resource_location: Leading slash all the way to but not including the ?
        :return: URI in a string.
        """
        return '{base}:{port}{location}'.format(base=self.host, port=self.port, location=resource_location)

class methods:
    """All HTTP methods in use"""

    @staticmethod
    def httpErrors(status_code):
        if status_code == 400:
            # Bad Request
            raise HTTPError.BadRequest('Bad Request. Check your data.') from None
        elif status_code == 401:
            # Unauthorized
            raise HTTPError.UnAuthorized('HTTP 401: Unauthorized; check your permissions or token.') from None
        elif status_code == 405:
            raise HTTPError.MethodNotAllowed('Wrong HTTP method used.') from None
        elif status_code != 200:
            raise HTTPError.UnKnownHTTPError('Unknown HTTP error occurred. Error {}'.format(status_code)) from None

    @staticmethod
    def get(url, sess):
        """Make a GET request"""
        r = sess.get(url)

        # Check for errors
        methods.httpErrors(r.status_code)

        # No news is good news
        return r

    @staticmethod
    def post(url, sess, data=None):
        """Make a POST request"""

        # dumps is there to ensure the data is properly formatted
        r = sess.post(url, data=json.dumps(data))
        # Check for errors
        methods.httpErrors(r.status_code)

        # No news is good news
        return r