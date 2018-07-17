# -*- coding:utf-8 -*-
from config import *
from thrall.amap import session

r = session.riding('116.434307,39.90909', destination=(116.434446,39.90816))
print(r.data)

