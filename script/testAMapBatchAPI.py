# -*- coding:utf-8 -*-
import pprint
from config import *
import utils
'''
There is something wrong in AMap Map API documentation.
we got {'info': 'INVALID_BATCH_PARAM', 'infocode': '20005', 'status': '0'} as documentation told.
'''
if __name__ == "__main__":
    query_str = f"/v3/batch?key={key}"
    payload = {
        "ops": [
            {
                "url": f"/v3/ip?ip=202.120.224.6&output=json&key={key}"
            },
            {
                "url": f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
            }
        ]
    }
    pprint.pprint(utils.post_to_amap(query_str, payload))
