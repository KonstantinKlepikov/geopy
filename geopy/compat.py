"""
Compatibility...
"""
import sys
py3k = sys.version_info >= (3, 0)

try:
    import json
except ImportError: # pragma: no cover
    try:
        import simplejson as json # pylint: disable=F0401
    except ImportError:
        from django.utils import simplejson as json # pylint: disable=F0401

assert json is not None

try:
    from BeautifulSoup import BeautifulSoup # pylint: disable=W0611,F0401
except ImportError: # pragma: no cover
    class BeautifulSoup(object): # pylint: disable=R0903
        """
        Raise import error.
        """

        def __init__(self):
            raise ImportError(
                "BeautifulSoup was not found. Please install BeautifulSoup "
                "in order to use the SemanticMediaWiki Geocoder."
            ) # pylint: disable=C0103

try:
    import oauth2 # pylint: disable=W0611,F0401
except ImportError:
    class oauth2(object): # pylint: disable=R0903
        """
        Raise import error.
        """

        def __init__(self):
            raise ImportError('No module named oauth2')
