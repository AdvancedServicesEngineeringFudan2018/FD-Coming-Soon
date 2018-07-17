# -*- coding:utf-8 -*-
import pprint
from contextlib import contextmanager
from requests.adapters import HTTPAdapter
from requests.sessions import Session
from requests.exceptions import (
    RequestException,
    ConnectionError,
    Timeout,
    HTTPError
)
from config import *
import utils
'''
Map API for AMAP
'''


class BaseRequest(object):
    def __init__(self, session=None):
        if not isinstance(session, Session):
            self.session = Session()
            self.session.mount('http://', HTTPAdapter(max_retries=1, pool_maxsize=50))
            self.session.mount('http://', HTTPAdapter(max_retries=1, pool_maxsize=50))
        else:
            self.session = session

    def get(self, url, params, timeout=1, callback=None, **kwargs):
        with self.catch_exception():
            r = self._get_result(url, params, timeout, **kwargs)
        if callable(callback):
            callback(r)
        return r

    def post(self, url, data, timeout=1, callback=None, **kwargs):
        with self.catch_exception():
            r = self._post_result(url, data, timeout, **kwargs)
        if callable(callback):
            callback(r)
        return r

    def _get_result(self, url, params, timeout, **kwargs):
        r = self.session.get(url, params=params, timeout=timeout, **kwargs)
        r.raise_for_status()
        return r

    def _post_result(self, url, data, timeout, **kwargs):
        r = self.session.post(url, data, timeout=timeout, **kwargs)
        r.raise_for_status()
        return r

    @contextmanager
    def catch_exception(self):
        try:
            yield
        except(ConnectionError, Timeout) as err:
            logger.error(str(err))
        except HTTPError as err:
            logger.error(str(err))
        except RequestException as err:
            logger.error(str(err))


class AMapRequest(BaseRequest):
    _BATCH_URL = '/v3/batch'
    _DISTRICT_URL = '/v3/config/district'

    def __init__(self, session=None):
        super(AMapRequest, self).__init__(session=session)
        print("__init__ done")

    def _url_swith(self, oru, dfu, url):
        if oru:
            return oru
        else:
            return url or dfu

    def get_data(self, p, default_url, url=None, **kwargs):
        params = p.params
        url = self._url_swith(url, default_url, p.DEFAULT_URL)
        return self.get(url.https_url if self._is_https else url.url,
                        params=params, **kwargs)

    def get_geo_code(self, p, **kwargs):
        return self.get_data(p, default_url=GEO_CODING_URL, **kwargs)

    def get_regeo_code(self, p, **kwargs):
        return self.get_data(p, default_url=REGEO_CODING_URL, **kwargs)

    def get_search_text(self, p, **kwargs):
        return self.get_data(p, default_url=POI_SEARCH_TEXT_URL, **kwargs)

    def get_search_around(self, p, **kwargs):
        return self.get_data(p, default_url=POI_SEARCH_AROUND_URL, **kwargs)

    def get_suggest(self, p, **kwargs):
        return self.get_data(p, default_url=POI_SUGGEST_URL, **kwargs)

    def get_district(self, p, **kwargs):
        return self.get_data(p, default_url=DISTRICT_URL, **kwargs)

    def get_distance(self, p, **kwargs):
        return self.get_data(p, default_url=DISRANCE_URL, **kwargs)

    def get_riding(self, p, **kwargs):
        return self.get_data(p, default_url=NAVI_RIDING_URL, **kwargs)

    def get_walking(self, p, **kwargs):
        return self.get_data(p, default_url=NAVI_WALKING_URL, **kwargs)

    def get_driving(self, p, **kwargs):
        return self.get_data(p, default_url=NAVI_DRIVING_URL, **kwargs)

    def get_district(self, query_list):
        utils.get_from_amap(self._DISTRICT_URL, query_list)


if __name__ == "__main__":
    test_query_list = [
        f"/v3/ip?ip=202.120.224.6&output=json&key={key}",
        f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    ]
    mapRequest = AMapRequest()
    pprint.pprint(mapRequest.get_batch_data(test_query_list))
