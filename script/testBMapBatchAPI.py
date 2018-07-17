# -*- coding:utf-8 -*-
import hashlib
import urllib.parse
from config import *
import utils

queryStr = f"/direction/v2/transit?origin=40.056878,116.30815&destination=31.222965,121.505821&ak={ak}"

encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

rawStr = encodedStr + sk

sn = hashlib.md5(urllib.parse.quote_plus(rawStr).encode("utf-8")).hexdigest()

url = urllib.parse.quote(rootURLB + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
print(url)
import pprint
pprint.pprint(utils.get_from_url_return_json(url))
