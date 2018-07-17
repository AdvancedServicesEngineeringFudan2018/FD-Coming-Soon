# -*- coding:utf-8 -*-
import requests
from config import *

logging.basicConfig(filename="log.out", level=logging.DEBUG)


def get_from_url_return_json(url):
    response = requests.get(url, headers=headers)
    logger.debug(response.json())
    return response.json()


def post_data_to_url_return_json(url, data):
    response = requests.post(url, data=data, headers=headers)
    logger.debug(response.json())
    return response.json()
