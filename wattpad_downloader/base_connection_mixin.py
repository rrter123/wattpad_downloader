from urllib.request import urlopen, Request
from urllib.parse import urlsplit, urlunsplit, quote
from bs4 import BeautifulSoup


class BaseConnectionMixin:
    """Class that handles all wattpad connections"""

    # Fool everyone into thinking I'm a Firefox
    headers = {"User-Agent": "Mozilla/5.0"}

    # Copied Code from  Stackoverflow
    def _iri2uri(self, iri: str) -> str:
        """
        Convert an IRI to a URI (Python 3).
        Needed in case some non-ASCII characters are in the copied url
        """
        uri = ""
        if isinstance(iri, str):
            (scheme, netloc, path, query, fragment) = urlsplit(iri)
            scheme = quote(scheme)
            netloc = netloc.encode("idna").decode("utf-8")
            path = quote(path)
            query = quote(query)
            fragment = quote(fragment)
            uri = urlunsplit((scheme, netloc, path, query, fragment))

        return uri
    # Copied code end

    def _sanitize(self, link: str) -> str:
        return self._iri2uri(link)

    def _create_request(self, link: str) -> Request:
        return Request(self._sanitize(link), headers=self.headers)

    def get(self, link: str) -> BeautifulSoup:
        with urlopen(self._create_request(link)) as page:
            soup = BeautifulSoup(page, "html.parser")
        return soup
