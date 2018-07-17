# -*- coding:utf-8 -*-
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) ' +
    'AppleWebKit/537.36 (KHTML, like Gecko) ' +
    'Chrome/56.0.2924.87 Safari/537.36',
    'content-type': 'application/json'
}

"""
We don't need to worry about the apikey leak in github.
Since I find these keys in github directly and it won't leak any message on me.
"""
# Map API for AMAP
rootURLA = "https://restapi.amap.com"
# Limit (times per day)     concurrency(times per second)
# 2000                      50
key = '926a17cc977ea70424c8569cad4f720d'

# Map API for Baidu
rootURLB = "http://api.map.baidu.com"
# Access Key ID
ak = '08eUG0hbUTzFrCFyF2Bn6tSQ7UD0cCaH'
# Secret Access Key
sk = '4Gzbk6HSzMHkWjjXliEOGM7ZAVvpqg0U'
