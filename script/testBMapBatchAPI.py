# -*- coding:utf-8 -*-
import pprint

from config import *
import utils
'''
百度地图API不支持公交线路的查询
'''

if __name__ == "__main__":
    queryStr = f"/direction/v2/transit?origin=40.056878,116.30815&destination=31.222965,121.505821&ak={ak}"
    pprint.pprint(utils.get_from_baidu(queryStr))
    
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
    pprint.pprint(utils.get_from_amap(query_str))
