# -*- coding:utf-8 -*-
import pprint
from config import *
import utils
'''
Map Batch API for AMAP
'''


class MapBatchAPI:
    _POST_URL = '/v3/batch'

    def __init__(self):
        print("__init__ done")

    def get_data(self, query_list):
        payload = {
            'ops': [{'url': query} for query in query_list]
        }
        return utils.post_to_amap(self._POST_URL, payload)


if __name__ == "__main__":
    test_query_list = [
        f"/v3/ip?ip=202.120.224.6&output=json&key={key}",
        f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    ]
    mapBatchAPI = MapBatchAPI()
    pprint.pprint(mapBatchAPI.get_data(test_query_list))
