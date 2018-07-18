# -*- coding:utf-8 -*-

TRANSIT_URL = '/v3/direction/transit/integrated'
IP_URL = '/v3/ip'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) ' +
    'AppleWebKit/537.36 (KHTML, like Gecko) ' +
    'Chrome/56.0.2924.87 Safari/537.36',
    'content-type': 'application/json'
}

"""
We don't need to worry about the api key leak in github.
Since I find these keys in github directly and it won't leak any message on me.
"""
# Map API for AMAP
rootURLA = "https://restapi.amap.com"
# Limit (times per day)     concurrency(times per second)
# 2000                      50
key = u'26885a28149a9869440c89def18d09f6'

