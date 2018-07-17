# -*- coding:utf-8 -*-
import requests
from config import *

url = f"https://restapi.amap.com/v3/batch?key={key}"
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
url = f"https://restapi.amap.com/v3/ip?ip=202.120.224.6&output=json&key={key}"

response = requests.post(url, headers=headers, data=payload)
print(response.json())
