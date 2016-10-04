"""Exceptions for the API"""

class NoAuthenticationProvided(Exception):
    """No authentication was provided when instantiating the module."""
class InvalidToken(Exception):
    """Token is not valid."""

class HTTPError(Exception):
    """Generic HTTP Error"""
    class BadRequest(Exception):
        """The request is not valid; HTTP 400"""
    class UnAuthorized(Exception):
        """Unauthorized; HTTP 401"""
    class MethodNotAllowed(Exception):
        """Wrong HTTP method used; HTTP 405"""
    class UnKnownHTTPError(Exception):
        """HTTP Error catch all"""

