# -*- coding:utf-8 -*-
import requests
import pprint
import hashlib
import urllib.parse
from config import *


def _get_from_url_return_json(url):
    response = requests.get(url, headers=headers)
    logger.debug(response.json())
    return response.json()


def _post_data_to_url_return_json(url, data):
    response = requests.post(url, data=data, headers=headers)
    logger.debug(response.json())
    return response.json()


def get_from_amap(query_str):
    """
    
    :param query_str:
    example: f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    :return:
    """
    url = rootURLA + query_str
    return _get_from_url_return_json(url)


def get_from_baidu(query_str):
    """
    
    :param query_str:
    example: f"/direction/v2/transit?origin=40.056878,116.30815&destination=31.222965,121.505821&ak={ak}"
    :return:
    """
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + sk
    sn = hashlib.md5(urllib.parse.quote_plus(raw_str).encode("utf-8")).hexdigest()
    url = urllib.parse.quote(rootURLB + query_str + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    return _get_from_url_return_json(url)


