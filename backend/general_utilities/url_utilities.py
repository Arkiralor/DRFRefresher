from urllib.parse import urlparse, parse_qs, urlunparse
import re

import tldextract
from furl import furl

tld_ex: tldextract.TLDExtract = tldextract.TLDExtract(
    include_psl_private_domains=True)
tld_ex.update(fetch_now=True)


class UrlInfo(object):
    HTTP = "http"
    HTTPS = "https"

    def __init__(self, raw_url, scheme=None):

        if not raw_url:
            raise Exception("no proper url passed")

        self.raw_url = raw_url

        scheme = scheme or self.HTTP
        ul = self.parse_url(scheme)

        self.furl = furl(ul)
        self.clean_qry()
        self.tld_info = tld_ex(ul)

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url

    def parse_url(self, scheme):
        raw_url = self.raw_url.lower()

        if raw_url.startswith("://"):
            raw_url = raw_url.split("://")[1]

        if raw_url.startswith("//"):
            raw_url = raw_url.split("//")[1]

        if raw_url.startswith("/www."):
            raw_url = "/".join(raw_url.split("/")[1:])
            ul = f"{scheme}://{raw_url}"
        elif raw_url.startswith("www."):
            ul = f"{scheme}://{raw_url}"
        elif not raw_url.startswith(self.HTTP):
            ul = f"{scheme}://{raw_url}"
        else:
            ul = raw_url
        return ul

    @property
    def path(self):
        return self.furl.path.normalize()

    @property
    def protocol(self):
        return self.furl.scheme or self.HTTP

    @protocol.setter
    def protocol(self, schema):
        self.furl.scheme = schema

    @property
    def is_secure(self):
        """

        :rtype: bool
        """
        return self.protocol == self.HTTPS

    @property
    def full_domain(self) -> str:
        """
        returns complete domain of url without other components
        for https://www.credibase.com/ result will be www.credibase.com

        """
        resp = self.tld_info.registered_domain
        if self.tld_info.subdomain:
            resp = f"{self.tld_info.subdomain}.{self.tld_info.registered_domain}"
        return resp

    @property
    def base_url(self):
        url = self.full_domain
        return f"{self.protocol}://{url}"

    @property
    def domain_path(self):
        url = self.full_domain
        if self.path:
            url = url + self.path.__str__()
        return url

    @property
    def schemaless_url(self):
        url = self.full_domain
        if self.path:
            url = url + self.path.__str__()
        if self.query_str:
            url = f"{url}?{self.query_str}"
        return url

    @property
    def url(self):
        url = self.base_url

        if self.path:
            url = url + self.path.__str__()

        if self.query_str:
            url = f"{url}?{self.query_str}"

        return url

    @property
    def real_sub_domain(self):
        sub_domain = self.tld_info.subdomain
        if self.tld_info.subdomain.startswith('www'):
            sub_domain = self.tld_info.subdomain.split("www")[1]
        if sub_domain.startswith("."):
            sub_domain = ",".join(sub_domain.split(".")[1:])
        return sub_domain

    @property
    def query_str(self):
        query_str = str(self.furl.query)
        if query_str:
            return query_str
        else:
            return None

    def path_url(self, path):
        f = furl(path)
        return furl(self.url, query=f.querystr, path=f.pathstr).url

    def clean_qry(self):
        for q, v in list(self.furl.query.params.items()):
            if q.startswith("utm"):
                self.furl.query.remove(q)
        return self

    @property
    def url_filetype(self):
        """
        Input a URL and output the filetype of the file
        specified by the url. Returns None for no filetype.
        'http://blahblah/images/car.jpg' -> 'jpg'
        'http://yahoo.com'               -> None
        """
        if not self.path:
            return None

        path_chunks = [x for x in self.path.segments if len(x) > 0]
        last_chunk = path_chunks[-1].split('.')  # last chunk == file usually
        if len(last_chunk) < 2:
            return None
        file_type = last_chunk[-1]

        # Assume that file extension is maximum 5 characters long
        if len(file_type) <= 5:
            return file_type.lower()
        return None

    @classmethod
    def redirect_back(cls, url, source_domain):
        """
        Some sites like Pinterest have api's that cause news
        args to direct to their site with the real news url as a
        GET param. This method catches that and returns our param.
        """
        parse_data = urlparse(url)
        domain = parse_data.netloc
        query = parse_data.query

        # If our url is even from a remotely similar domain or
        # sub domain, we don't need to redirect.
        if source_domain in domain or domain in source_domain:
            return url

        query_item = parse_qs(query)
        if query_item.get('url'):
            # log.debug('caught redirect %s into %s' % (url, query_item['url'][0]))
            return query_item['url'][0]

        return url

    @classmethod
    def is_http_url(cls, url):
        """
        :return:
        """
        ## TODO: update this function according to rest
        if not re.compile(r'^https?://[^\s/$.?#].[^\s]*$', re.IGNORECASE).search(url):
            return False

        try:
            # Try parsing the URL
            uri = urlparse(url)
            _ = urlunparse(uri)
        except Exception as ex:
            raise ex

        if not uri.scheme or not uri.scheme.lower() in ['http', 'https'] or not uri.hostname:
            return False

        return True

    def domain_redirect(self, source_domain):
        return self.tld_info.registered_domain != source_domain

    def path_redirect(self, source):
        return self.path != source.path or self.query_str != source.query_str
