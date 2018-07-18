# -*- coding:utf-8 -*-
import pprint
import urllib.parse
from const import *
import map_api

'''
Map Batch API for AMAP
'''


class MapBatchAPI:
    __BATCH_URL = '/v3/batch'

    def get_data(self, service_url, query_list):
        payload = {
            'ops': [
                {'url': f"{service_url}?key={key}&{urllib.parse.urlencode(query, safe=',')}"}
                for query in query_list
            ]
        }
        # print(payload)
        return map_api.post_to_amap(self.__BATCH_URL, payload)

    def get_ip_data(self, query_list):
        return self.get_data(IP_URL, query_list)

    def get_transit_data(self, query_list):
        return self.get_data(TRANSIT_URL, query_list)


if __name__ == "__main__":
    test_query_list = [
        {
            "ip": "202.120.224.6",
            "output": "json"
        },
        {
            "ip": "202.120.224.26",
            "output": "json"
        },
    ]
    mapBatchAPI = MapBatchAPI()
    pprint.pprint(mapBatchAPI.get_ip_data(test_query_list))
    pprint.pprint(mapBatchAPI.get_ip_data([{}]))

    test_transit_query = [
        {
            "origin": "116.481499,39.990475",
            "destination": "116.465063,39.999538",
            "city": "021",
            "nightflag": "1",
            "output": "json"
        },
        {
            "origin": "120,30",
            "destination": "120,30",
            "city": "021",
            "nightflag": "1",
            "output": "json"
        }
    ]
    pprint.pprint(mapBatchAPI.get_transit_data(test_transit_query))
