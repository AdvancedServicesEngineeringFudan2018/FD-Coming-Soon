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

# 高德API
# 调用量上限（次/日）    并发量上限（次/秒）
# 2000                50
key = '5f1f377483e342c20fc4005f31a436a8'
