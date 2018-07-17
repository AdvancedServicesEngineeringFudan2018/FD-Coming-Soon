# -*- coding:utf-8 -*-
import pprint
from config import *
import utils
'''
高德批量请求接口的API文档有误，照着跑不出
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
    pprint.pprint(utils.get_from_amap(query_str))
