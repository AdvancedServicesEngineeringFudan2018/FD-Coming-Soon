# -*- coding:utf-8 -*-
import requests
import json
from config import *


def __get_from_url_return_json(url):
    """

    :param url: whole url
    :return:
    """
    response = requests.get(url, headers=headers)
    logger.debug(response.json())
    return response.json()


def __post_data_to_url_return_json(url, data):
    """

    :param url: whole url
    :param data: json dict{}
    need to be transformed into `json.dumps(data)`
    :return:
    """
    response = requests.post(url, data=json.dumps(data), headers=headers)
    logger.debug(response.json())
    return response.json()


def get_from_amap(query_str):
    """
    
    :param query_str: format string in python3.6
    example: f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    :return:
    """
    url = rootURLA + query_str
    return __get_from_url_return_json(url)


def post_to_amap(query_str, data):
    """

    :param query_str: format string in python3.6
    example: f"/v3/ip?ip=202.120.224.26&output=json&key={key}"
    :param data: json dict{}
    :return:
    """
    url = rootURLA + query_str
    return __post_data_to_url_return_json(url, data=data)
