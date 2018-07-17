# -*- coding:utf-8 -*-
import requests
import hashlib
import json
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


def post_to_amap(query_str, data):
    """

    :param query_str:
    example: f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    :param data:
    :return:
    """
    url = rootURLA + query_str
    return _post_data_to_url_return_json(url, data=json.dumps(data))
