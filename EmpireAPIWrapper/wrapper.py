import requests
from .Exceptions import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class empireAPI(object):

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

        # If token is provided, check the version
        if token is not None:
            self._checkToken()
